import os
from dotenv import load_dotenv
import msal
import requests

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["User.Read", "Directory.Read.All"]

# Validate that required environment variables are set
if not all([CLIENT_ID, TENANT_ID]):
    raise ValueError("Please set CLIENT_ID and TENANT_ID in .env file")

# Create MSAL public client
app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

# Acquire token via device code flow
flow = app.initiate_device_flow(scopes=SCOPES)
if "user_code" not in flow:
    raise Exception("Failed to create device flow")

print(f"Go to {flow['verification_uri']} and enter code: {flow['user_code']}")
result = app.acquire_token_by_device_flow(flow)

if "access_token" in result:
    headers = {"Authorization": f"Bearer {result['access_token']}"}

    # Get signed-in user info
    user_response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
    user_data = user_response.json()
    print("\n👤 User Info:")
    print(f"Name: {user_data.get('displayName')}")
    print(f"Email: {user_data.get('mail') or user_data.get('userPrincipalName')}")

    # Get tenant info (via organization endpoint)
    tenant_response = requests.get("https://graph.microsoft.com/v1.0/organization", headers=headers)
    tenant_data = tenant_response.json()
    print("\n🏢 Tenant Info:")
    print(f"Name: {tenant_data['value'][0].get('displayName')}")
    print(f"Tenant ID: {tenant_data['value'][0].get('id')}")

    # Optional: List users
    users_response = requests.get("https://graph.microsoft.com/v1.0/users", headers=headers)
    users_data = users_response.json()
    print("\n📋 Users in Tenant:")
    for user in users_data.get("value", []):
        print(f"- {user.get('displayName')} ({user.get('userPrincipalName')})")
else:
    print("❌ Failed to authenticate:", result.get("error_description"))
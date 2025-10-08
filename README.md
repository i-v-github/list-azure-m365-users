# Azure User Listing Tool

A Python script to list users from Azure Active Directory (Azure AD) using Microsoft Graph API.

## Prerequisites

- Python 3.12 or higher
- Azure AD application with appropriate permissions
- Required Python packages (see `requirements.txt`)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd list_azure_users
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your Azure AD credentials:
   ```
   CLIENT_ID=your_client_id
   TENANT_ID=your_tenant_id
   ```

## Usage

Run the script:
```bash
python list_azure_users.py
```

## Configuration

Modify the script to adjust the query parameters or output format as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

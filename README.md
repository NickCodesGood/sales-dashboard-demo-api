# Django Backend Setup

Welcome to the backend repository for sales-dashboard-demo, built using Python + Django.

## Pre-requisites

- Python (>= 3.8)
- pip (Python's package installer)

## Installation & Setup

Follow these steps to set up the Django backend on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/NickCodesGood/sales-dashboard-demo-api/
cd sales-dashboard-demo-api
```

### 2. Setup a Virtual Environment (Optional)

Python 3 comes with a built-in module named `venv` to create virtual environments. 

To create a virtual environment:

```bash
python3 -m venv venv
```

To activate the virtual environment:

On macOS and Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

## Model and View Overview

This Django backend is primarily built around the `Lead` model which manages potential business leads.

### Model: Lead

Fields:

- `name`: Text field for the lead's name.
- `email`: Unique email field.
- `status`: Char field with choices (prospect, active, unqualified) with a default value of 'prospect'.
- `estimatedSaleAmount`: Decimal field with a max of 1 trillion + 0.00 cents.
- `estimatedCommission`: A computed decimal field based on the `estimatedSaleAmount` and lead status.

This model also overrides the save method to compute the `estimatedCommission` based on the lead status and `estimatedSaleAmount`.

### Views

#### 1. ItemListCreateView

- Type: List and Create API View
- Model: Lead
- Serializer: LeadSerializer
- Authentication: Required
- Pagination: CustomPagination (5 items per page, can be adjusted with a query parameter)

#### 2. ItemRetrieveUpdateDestroyView

- Type: Retrieve, Update, and Destroy API View
- Model: Lead
- Serializer: LeadSerializer
- Authentication: Required

#### 3. Login

This is a custom view to handle user login. Upon successful authentication, a token is generated and returned. If the authentication fails, an "Invalid credentials" response is given.

## Important Settings

- `INSTALLED_APPS` includes essential Django apps, rest_framework for the DRF setup, rest_framework.authtoken for token-based authentication, corsheaders for handling Cross-Origin Resource Sharing, and your custom app 'crm'.
- Middleware settings include standard Django middleware and the CorsMiddleware for handling CORS.
- `DATABASES` is set up to use PostgreSQL. Make sure you replace the placeholder password with your real database password. Ensure that your credentials are stored securely in a production environment.

## Additional Notes

Always ensure your database credentials are kept securely. Avoid hardcoding them directly in the `settings.py`. Instead, consider using environment variables or a secrets management solution, especially for production setups.

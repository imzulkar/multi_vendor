# Django Application Setup Guide

## Prerequisites

- Python (3.10 recommended)
- Pip (Python package installer)
- Virtualenv or a similar virtual environment tool
- A database server (e.g., PostgreSQL, MySQL, SQLite)
- Redis (for Celery)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/imzulkar/multi_vendor.git
cd multi_vendor
```

2. Create a virtual environment and activate it:

```bash
virtualenv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

# Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

Access the application in your web browser at http://localhost:8000.

# Running Celery Worker and Beat

1. Make sure Redis server is running (if you're using Celery with Redis).

2. Start Celery worker:

```bash
celery -A config worker --loglevel=info eventlet
```

3. Start Celery beat:

```bash
celery -A config beat --loglevel=info
```

##User credentials 

###Seller Accounts:
```bash
Username: seller1, 
Password: seller1@123

Username: seller2, 
Password: seller2@123
```
###Customer Accounts:
```bash
Username: customer1, 
Password: customer1@123

Username: customer2, 
Password: customer2@123
```

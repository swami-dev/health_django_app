# Healthcare Project

This project is a Django-based web application for managing user registration, authentication, and profile management for a healthcare system. It includes features such as user registration, login, and a simple dashboard for user accounts.

## Features

- User Registration with validation for secure passwords.
- User Login and Logout functionality.
- Customizable user profiles with support for profile pictures.
- Responsive design with a clean and professional interface.

## Requirements

asgiref==3.8.1
Django==5.1.5
djangorestframework==3.15.2
pillow==11.1.0
sqlparse==0.5.3
Bootstrap (for front-end design)

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/swami-dev/healthcare_project.git
cd healthcare_project
```

### Step 2: Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run the Development Server
```bash
python manage.py runserver
```

### Step 6: Access the Application
Open your browser and navigate to: `http://127.0.0.1:8000/`

## Directory Structure

```
healthcare_project/
├── manage.py
├── project_main/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       ├── register.html
│   │       └── home.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── requirements.txt
```

## Configuration

### Media Files
To enable profile picture uploads, configure the following in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Add the following to `urls.py` to serve media files during development:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Usage

### Register a User
1. Navigate to `http://127.0.0.1:8000/users/register/`
2. Fill out the registration form and submit.

### Login
1. Navigate to `http://127.0.0.1:8000/users/login/`
2. Enter your username and password.

### Access Dashboard
1. After login, you'll be redirected to the dashboard.

### Logout
1. Click the logout button in the dashboard to sign out.

## Customization

### Password Validation
Password validation rules can be customized in `settings.py` under the `AUTH_PASSWORD_VALIDATORS` setting. For example:

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        },
    },
]
```

### Frontend Design
The application uses Bootstrap for styling. You can customize the templates in the `users/templates/users/` directory.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy using the Healthcare Project!

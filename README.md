# Profiles

A simple social auth app for creating, updating, deleting user profiles.

# Getting started

- Clone the project.
- Make a virtual environment.
- Run `make build` to install dependencies and prepare the db.
- Create a superuser (https://docs.djangoproject.com/en/4.1/ref/django-admin/#createsuperuser)
- Run `make runserver` to start the application.
- Add a new social app;
    - Navigate to http://127.0.0.1:8000/admin/socialaccount/socialapp/add/
    - Choose `GitHub` as a provider;
    - Add a `Client id`;
    - Add a `Secret key`;
    - Choose `example.com` from Sites;
    - `Save` your changes.
- Navigate to http://127.0.0.1:8000/accounts/github/login/ to authenticate with GitHub.

# Testing

- Run `make pytest` to run the tests.
- Run `make coverage` for coverage report.
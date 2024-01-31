# Simple Blog Application

## Overview

This is a simple blog application developed using Django. Users can sign up, log in, and log out to create and manage their blog posts. Authenticated users can perform CRUD operations (Create, Read, Update, Delete) on blog posts, and all users can view the list of blog posts on the home page.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Blog Post Management**: Authenticated users can create, read, update, and delete blog posts.
- **Viewing Blog Posts**: All users can view the list of blog posts on the home page and click on individual posts to view details.
- **Administration Panel**: Admins can manage blog posts using Django's built-in admin panel.

## Setup and Installation

1. Create a Django Project

    django-admin startproject simple_blog
    cd simple_blog_


2. Create a Django App

    python manage.py startapp blog1


3. Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate   # On Windows


4. Install dependencies:

    pip install -r requirements.txt
    

5. Apply migrations:

    python manage.py makemigrations
    python manage.py migrate
    

6. Create a superuser:

    python manage.py createsuperuser


7. Run the development server:

    python manage.py runserver
    

8. Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- **Sign Up**: Users can sign up for a new account.
- **Log In**: Existing users can log in to their accounts.
- **Create Post**: Authenticated users can create new blog posts.
- **Edit/Delete Post**: Authenticated users can edit or delete their own blog posts.
- **View Posts**: All users can view a list of blog posts on the home page and click on individual posts to view details.
- **Admin Panel**: Admins can access the Django admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage blog posts.

## Technologies Used

- Django
- HTML


"""Lesson Notes - Setting up a Django Project"""

# ! cmd to create project --> django-admin startproject django_project_name

# ! Activate virtual environment --> env_name\Scripts\activate
# ! To run a django project --> python manage.py runserver
# ! To create an app --> python manage.py startapp app_name

# ? CLI Commands for Live Server:
# python manage.py runserver --> runs the development server on the default port 8000.
#

# manage.py --> is a command line utility that helps you run Django related tasks.
# It is automatically created when you start a new Django project.

# ? --------------------------------------------------------------------------------------------------------------------

# ? The first_django_project folder contains built in files:

# __init__.py --> is an empty file that tells Python that this directory should be considered a Python package.
# settings.py --> contains all the settings and configurations for your Django project.
# urls.py --> is where you define the URL patterns for your project.

# WSGI (Web Server Gateway Interface):
# wsgi.py --> is used for deploying your project on a web server.

# ASGI (Asynchronous Server Gateway Interface):
# asgi.py --> is used for deploying your project on an ASGI server, which is an alternative to WSGI and is
# designed for handling asynchronous web applications.

# Difference between synchronous and asynchronous:
# Synchronous code executes sequentially, meaning that each operation must complete before the next one starts
# Asynchronous code allows multiple operations to run concurrently, meaning that one operation can start
# before the previous one finishes.

# ? --------------------------------------------------------------------------------------------------------------------

# ? Synchronous (WSGI is synchronous):
# def f1():
#     pass

# def f2():
#     pass

# ? Characteristics of synchronous code:
# Handles only synchronous requests
# Only one request can be handled at a time per worker
# Simple and stable
# Used for traditional web applications

# If we call f1() and f2(), f1() will execute first and only after it finishes, f2() will start executing.

# ? --------------------------------------------------------------------------------------------------------------------

# ? Asynchronous (ASGI is asynchronous):
# async def f1():
#     pass

# async def f2():
#     pass

# If we call f1() and f2(), both functions can run concurrently, meaning that they can start executing at the same time,
# and they can interleave their execution. This allows for more efficient use of resources and can improve the
# performance of web applications.

# ? Characteristics of asynchronous code:
# Handles asynchronous requests
# Multiple requests can be handled concurrently
# Real time features

# Request ---> Server ---> ASGI Worker ---> Response ---> Client

# ? --------------------------------------------------------------------------------------------------------------------

# ? settings.py:
# This file contains all the settings and configurations for your Django project.
# It includes settings for database configuration, installed apps, middleware, templates, static files, and more.

# You can customise this file to suit the needs of your project:

# from pathlib import Path - is used to handle file paths in a platform-independent way.

# BASE_DIR = Path(__file__).resolve().parent.parent - defines the base directory of the project, which is used to
# construct paths for other files and directories in the project.
# Build paths inside the project like this: BASE_DIR / 'subdir'.

# SECRET_KEY = ' - is a secret key used for cryptographic signing in Django. It should be kept secret in production.
# You can change this key to something unique and secure for your project.

# DEBUG = True - is a setting that enables or disables debug mode. In debug mode, Django will display detailed error
# pages when an error occurs. It should be set to False in production for security reasons.

# ALLOWED_HOSTS = [] - is a list of strings representing the host/domain names that this Django site can serve.
# This is a security measure to prevent HTTP Host header attacks. You should add your domain names or IP addresses
# to this list when deploying your project.

# INSTALLED_APPS = [ - is a list of strings designating all applications that are enabled in this Django installation.
# Each string should be a dotted Python path to an application configuration class, or package containing an application
# You can add your own apps to this list when you create them.

# MIDDLEWARE = [ - is a list of middleware to use. Middleware are hooks into Django's request/response processing.
# Each middleware component is responsible for doing some specific function. You can add your own middleware to this
# list when you create them.

# ROOT_URLCONF = 'first_django_project.urls' - is a string representing the full Python import path to the root URL
# configuration.
# This tells Django which module to use for URL routing. You can change this if you want to use a different URL
# configuration.

# TEMPLATES = [ - is a list of template engine configurations. Each configuration is a dictionary containing settings
# for a specific template engine. The default configuration uses the Django template engine. You can add
# additional template engines or customise the existing one as needed.

# WSGI_APPLICATION = 'first_django_project.wsgi.application' - is a string representing the full Python import path
# to the WSGI application callable that Django's built-in servers (e.g., runserver) will use. This is used for deploying
# your project on a WSGI server. You can change this if you want to use a different WSGI application or if you are
# deploying on an ASGI server instead.

# DATABASES = { - is a dictionary containing the settings for all databases to be used with this Django installation.
# The default configuration uses SQLite, but you can change this to use other databases like PostgreSQL, MySQL, etc.

# AUTH_PASSWORD_VALIDATORS = [ - is a list of validators that are used to validate user passwords. You can add or remove
# validators as needed.

# LANGUAGE_CODE = 'en-us' - is a string representing the language code for this installation. This is used for
# internationalisation and localisation. You can change this to use a different language code.
# For UK English, you would use 'en-gb'.

# STATIC_URL = 'static/' - is a string representing the URL to use when referring to static files (CSS, JavaScript,
# images). You can change this if you want to use a different URL for static files.

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' - is a string representing the default type of primary key
# to use for models that don't have a field with primary_key=True. You can change this if you want to use a different
# type of primary key for your models.
# It is not present in the latest version of Django, because it is now the default behavior to use BigAutoField for
# primary keys. If you want to use a different type of primary key, you can specify it in your model definition instead
# of changing the default in settings.py.

# ? --------------------------------------------------------------------------------------------------------------------

# ? Other Project files:

# ? manage.py:
# This file is a command-line utility that helps you run Django related tasks. It is automatically created when you
# start a new Django project. You can use it to run the development server, create database migrations, and perform
# other administrative tasks.

# ? urls.py:
# This file is where you define the URL patterns for your project. It is used to route incoming HTTP requests to the
# appropriate views based on the URL. You can define URL patterns using regular expressions or path converters,
# and you can include URL patterns from your apps as well.

# ? wsgi.py:
# This file is used for deploying your project on a web server that supports WSGI. It contains the WSGI application
# callable that the server uses to communicate with your Django application.

# ? asgi.py:
# This file is used for deploying your project on an ASGI server, which is an alternative to WSGI and is designed for
# handling asynchronous web applications. It contains the ASGI application callable that the server uses to communicate
# with your Django application.

# ? __init__.py:
# This is an empty file that tells Python that this directory should be considered a Python package. It allows you to
# import modules from this directory in other parts of your project. It is automatically created when you start a new
# Django project and is required for Python to recognize the directory as a package.

# ? --------------------------------------------------------------------------------------------------------------------

# ? Projects and Apps:
# A Django project is a collection of settings and configurations for a web application. It can contain multiple apps,
# which are reusable components that provide specific functionality. For example, you might have an app for user
# authentication, another app for a blog, and another app for an e-commerce store. Each app can be developed and
# maintained independently, and can be reused across different projects. When you create a new app using the command
# python manage.py startapp app_name, it will create a new directory with the necessary files for that app, including
# models.py, views.py, urls.py, and more.

# ? Files in an App:
# models.py --> is where you define the data models for your app. This is where you define the structure of your
# database tables and the relationships between them.

# views.py --> is where you define the views for your app. Views are functions or classes that handle HTTP requests and
# return HTTP responses. They are responsible for processing user input, interacting with the database, and rendering
# templates.

# admin.py --> is where you register your models with the Django admin site. This allows you to manage your data through
# a web interface provided by Django.

# apps.py --> is where you define the configuration for your app. This is where you can specify the name of your app and
# any other settings related to it.

# tests.py --> is where you write tests for your app. This is where you can define test cases to ensure that your app is
# working correctly and to catch any bugs or issues before they affect users.

# __init__.py --> is an empty file that tells Python that this directory should be considered a Python package.
# It allows you to import modules from this directory in other parts of your project.

# urls.py --> is where you define the URL patterns for your app. This is where you can specify the URLs that will be
# handled by your app and the views that will be called when those URLs are accessed.

# ? --------------------------------------------------------------------------------------------------------------------

# ? DTL is the django template language - a presentation-layer language
# It's used to display dynamic data in html
# It allows us to use:
# Show variables
# Use loops
# Use conditional statements
# Extend templates
# Use filters

# ? --------------------------------------------------------------------------------------------------------------------

# ? CSRF (Cross-Site Request Forgery) is a security vulnerability that allows an attacker to trick a user into
#   performing actions on a web application without their consent.

#  Django has built-in protection against CSRF attacks,
#  which is enabled by default. When you use the {% csrf_token %} template tag in your forms, Django will generate a
#  unique token for each form and include it as a hidden field. When the form is submitted, Django will check that the
#  token is valid and matches the token stored in the user's session. If the token is missing or invalid, Django will
#  reject the request and return a 403 Forbidden response. This helps to prevent CSRF attacks by ensuring that
#  only legitimate requests from the user's browser are accepted by the server.

# ? --------------------------------------------------------------------------------------------------------------------

# ? Django Admin Panel:

# To stop the server (to make changes to code and restart):
# Press Ctrl + C in the terminal where the server is running.
# python manage.py makemigrations
# python manage.py migrate

# To create credentials for Admin panel:
# python manage.py createsuperuser
# python manage.py runserver

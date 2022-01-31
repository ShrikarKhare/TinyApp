# TinyApp Project

Ever feel like you're copy pasting links that are too long? TinyApp is a full stack web application built with Python and Django that allows users to shorten long URLs (à la bit.ly).

# Link to Deployed App

[TinyApp](http://shrikarK.pythonanywhere.com)
** Link active till end of April 2022 **

## Final Product

!["Login Page"](https://github.com/ShrikarKhare/TinyApp/Images/LandingPage.JPG)
!["screenshot description"](# Main login page)

## Dependencies

- asgiref
- bcrypt
- beautifulsoup4
- cffi
- Django
- django-bootstrap-v5
- django-crispy-forms
- django-environ
- psycopg2
- pycparser
- six
- soupsieve
- sqlparse
- tzdata


## Getting Started

- Set up a virtual environment
- Install all dependencies (using the pip install requirements.txt command).
- Set up a postgres or sqlite database.  If a postgres database is being used, make sure to populate the secrets in a .env file
- Run the development web server using the `python manage.py runserver` command.
- Run the migrations using the `python manage.py migrate` command.
- Create a superuser to access the /admin page
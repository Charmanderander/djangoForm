# djangoForm
Customized form for issue tracking

There will be three pages
1) Open issues
2) Closed issues
3) A collection of scripts that were written
4) A submission page

Look at the sketch for more details

# Getting it to run

1) Pull the project
2) pip install -r requirements.txt
3) Ensure Postgres Database is running
  - You can change the ports under settings.py
4) python manage.py makemigrations / migrate (if needed)
5) python manage.py runserver

# External Software Dependencies

1) Install postgresql DB
    - Change the user name and password of your database in settings.py
    - Remember to run "python manage.py makemigrations / migrate" !

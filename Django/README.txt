CURRENT VIDEO - https://www.youtube.com/watch?v=Dv15y5CgCyE&index=25&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK

#Server
python manage.py runserver - starts local server

#DataBase
python manage.py makemigrations - creates migrations
python manage.py makemigrations [appname] - creates migrations for [appname]
python manage.py migrations - apply migrations to DB
python manage.py createsuperuser - create and admin user for DB
python manage.py sqlmigrate [appname] [migrationcode] - gets information about migration code specified from the app specified

#Project
django-admin startproject [projectname] - creates project folder with startup files named [projectname]
python manage.py shell - runs django shell

#Django
[ClassName].objects.all() - gets all rows from DB
[ClassName].objects.filter(id=1) - filters all rows by id
[ClassName].objects.filter(artist__startswith='Taylow') - filters all rows by artist name and returns every row which artist field starts with Talor

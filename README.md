# django-CS50
CS50: DJANGO TUTORIAL\

(Note: Create Virtual Environment if necessary)\
Python version: 3.9.2 \
Django version: 3.1

NOTES:\
(taken during the course)

Commands:\
-Creating our first project using commands:\
django-admin startproject projectName\
-Creating our first app using commands:\
python manage.py startapp appName\
-Running our computer as server:\
python manage.py runserver

First App:\
-Produce a response (HttpResponse) when a url is visited.\
-urls.py in project folder: master urls.py file connects with urls in apps\
-urls.py in app folder: creating this file allows us to separate things out (modularity).\
-Each url will display a different HttpResponse.\
-We can create url patterns using placeholders and take extra arguments.\
-We can use python logic in those placehoders to modify the content displayed.

Http Response & Render:\
-HttpResponse : can display html content.\
-Render : can render an entire html file.\
Using render our content is clear and makes easier collaborations.

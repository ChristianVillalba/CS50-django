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
-We can create url patterns using placeholders [<str:name>] and take extra arguments.\
-We can use python logic in those placehoders to modify the content displayed.

Http Response & Render:\
-HttpResponse : can display html content.\
-Render : can render an entire html file.\
Using render our content is clearer and makes easier collaborations.
+Render takes two args:\ 
request: makes a reference to the http request the user will make.\
template name: a reference to what are going to use.\
Render best practice: prefix the file with the directory name to avoid conflicts:\
eg: render(request, "myDirectory/myFile.html")

Templates:\
-Templates are parameterizables\
Django takes html files and treats them like templates that we can render\ 
adding its own template language on top of the existing html.\
-{{ }} Django template language, injects content.\
The content will be a variable created using a python dictionary {key:VALUE} \
In the html: {{key}} will display the VALUE\
+eg: hello application\
-{% %} Django template language, adds logic.\
The content displayed will depend on the logic (eg: conditions).\
Django takes the html files, manipulate them and returns only the final result.\
Logic and possible content won't be displayed using devTools\
+eg: newyear application 



# django-CS50
#### CS50: DJANGO TUTORIAL

(Create Virtual Environment if necessary)      
Python version: 3.9.2    
Django version: 3.1

What Python version can I use with Django?:    
https://docs.djangoproject.com/en/3.2/faq/install/

[in Terminal]    
Check python version: python 
Check django verion: python -m django --version



#### DJANGO PROJECT:
A Django Project ususally consisit in one or more Django Applications.   
Each Application will offer a different service or functionality inside our bigger project.   
I created this project to understand how Django works:   

#### Project:
#### -Lecture3

#### Applications:
#### -hello App
It returns a response when we visit *localServer*/hello  
Inside this app, I included the next options:  
*localServer*/hello/ [It renders an html template: index.html]  
*localServer*/hello/cristian [an http response]  
*localServer*/hello/cthulhu  [an http response]  
*localServer*/hello/*name*  [It renders an html template (greet.html) that uses placeholders]  
#### -newyear App
It returns Yes or No depending if the current day is New Year.
*localServer*/newyear
#### -tasks App     
A Task Management App.   
It returns a list of taks and we can delete Items.   
It uses a form to add new tasks.    
It uses sessions to personalise what is displayed to each different user   

## NOTES:
These notes were taken during the lecture:    
*Django - Lecture 3 - CS50's Web Programming with Python and JavaScript 2020*      
Link (YouTube) : https://www.youtube.com/watch?v=w8q0C-C1js4&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=5&ab_channel=CS50  
The next notes are just references of what I considered useful information related to this project.   
Good written documentation is a key part of Django:   
Link (Django Documentation): https://www.djangoproject.com/

Commands:   
-Creating our first project using commands:   
django-admin startproject projectName   
-Creating our first app using commands:   
python manage.py startapp appName   
-Running our computer as server:   
python manage.py runserver

[To be able to use any app: go to settings.py >scroll> INSTALLED_APPS > add nameApp to the list.]

Basic Response - hello app 
-Produce a response (HttpResponse) when a url is visited.   
-urls.py in project folder: master urls.py file connects with urls in apps   
-urls.py in app folder: creating this file allows us to separate things out (modularity).   
-Each url will display a different HttpResponse.   
-We can create url patterns using placeholders [<str:name>] and take extra arguments.   
-We can use python logic in those placehoders to modify the content displayed.

Http Response & Render:    
-HttpResponse : can display html content.   
-Render : can render an entire html file.   
Using render our content is clearer and makes easier collaborations.    
+Render takes two args (arguments):   
request: makes a reference to the http request the user will make.   
template name: a reference to what are going to use.   
Render best practice: prefix the file with the directory name to avoid conflicts:   
eg: render(request, "myDirectory/myFile.html")

Templates & Static Files:   
Best practice: How to manage the folders to keep all the processes separated and manage modularity:   
projectFolder/appName/templates/appName/index.html   
projectFolder/appName/static/appName/style.css

Templates:   
-Templates are parameterizables   
Django takes html files and treats them like templates that we can render   
adding its own template language on top of the existing html.   
-{{ }} Django template language, injects content.   
The content will be a variable created using a python dictionary {key:VALUE}    
In the html: {{key}} will display the VALUE   
*eg: hello application*   
-{% %} Django template language, adds logic.   
The content displayed will depend on the logic (eg: conditions).   
Django takes the html template and manipulate it based on the input we get.   
then, it returns to the user only the final result at the end of the rendering process.   
Logic and possible content won't be displayed using devTools   
*eg: newyear application* 

Static Files:   
Files that aren't going to change (eg: CSS or JS).
Django can generate dynamic html using python logic or inject static files.

Generating Dynamic Content : task app    
It shows us a list of taks, we can add more and it shows the new additions.    
Using a context dictionary in our views.py (Usually in the context dictionary, the keys and values have the same name),    
Django have access to the variable name "tasks" that contains the value tasks. {"tasks":tasks}
We can create an index.html file that uses the variable "tasks"     
And adding a for loop to our template...
...the displayed content (our list) will be dynamic.





## NOTES: Lecture3
These notes were taken during the lecture:    
*Django - Lecture 3 - CS50's Web Programming with Python and JavaScript 2020*      
Link (YouTube) : https://www.youtube.com/watch?v=w8q0C-C1js4&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=5&ab_channel=CS50  
The next notes are just references of what I considered useful information related to this project.   
Good written documentation is a key part of Django:   
Link (Django Documentation): https://www.djangoproject.com/

#### Commands:   
-Creating our first project using commands:   
django-admin startproject projectName   
-Creating our first app using commands:   
python manage.py startapp appName   
-Running our computer as server:   
python manage.py runserver

[To be able to use any app: go to settings.py >scroll> INSTALLED_APPS > add nameApp to the list.]

#### Basic Response - hello app
-Produce a response (HttpResponse) when a url is visited.   
-urls.py in project folder: master urls.py file connects with urls in apps   
-urls.py in app folder: creating this file allows us to separate things out (modularity).   
-Each url will display a different HttpResponse.   
-We can create url patterns using placeholders [<str:name>] and take extra arguments.   
-We can use python logic in those placeholders to modify the content displayed.

#### Http Response & Render:    
-HttpResponse : can display html content.   
-Render : can render an entire html file.   
Using render our content is clearer and makes easier collaborations.    
+Render takes two args (arguments):   
request: makes a reference to the http request the user will make.   
template name: a reference to what are going to use.   
Render best practice: prefix the file with the directory name to avoid conflicts:   
eg: render(request, "myDirectory/myFile.html")

#### Templates & Static Files:   
Best practice: How to manage the folders to keep all the processes separated and manage modularity:   
projectFolder/appName/templates/appName/index.html   
projectFolder/appName/static/appName/style.css


#### Templates:   
-Templates are parameterizables   
Django takes html files and treats them like templates that we can render   
adding its own template language on top of the existing html.   

-{{ }} Django template language, injects content.   
*eg: hello application*    
The content will be a variable created using a python dictionary {key:VALUE}    
In the html: {{key}} will display the VALUE assigned in our python file.   

-{% %} Django template language, adds logic.   
*eg: newyear application*     
The content displayed will depend on the logic (eg: conditions).   
Django takes the html template and manipulate it based on the input we get.   
then, it returns to the user only the final result at the end of the rendering process.   
Logic and possible content won't be displayed using devTools   

#### Static Files:   
Files that aren't going to change (eg: CSS or JS).
Django can generate dynamic html using python logic or inject static files.

#### Generating Dynamic Content : task app    
It shows us a list of tasks, we can add more and it shows the new additions.    
Using a context dictionary in our views.py (Usually in the context dictionary, the keys and values have the same name),    
Django have access to the variable name "tasks" that contains the value tasks. {"tasks":tasks}    
We can create an index.html file that uses the variable "tasks"     
And adding a for loop to our template...
...the displayed content (our list) will be dynamic.

#### Template Inheritance:

We can define an html layout that the others html files (index & addtask) are going to inherit from it.    
This allows us to have the same structure in all the files. (Consistency between our pages).     
*eg: layout.html in our tasks application*     
*index.html & addtasks.html inherit the content from layout.html using* {% extends "tasks/layout.html" %}       
Be able to factor out the html that is common to all the pages can be very helpful just for good design and not repeat ourselves and makes it easier to change the common structure.     

#### Using urls with Django

Change the pages in our website is a bit hard,     
Django is designed to make easy change the structure of the pages in terms of how the urls are related to each other.     
This is based on the content of the urls.py file      
We don’t need to hard code all the links. Django have a feature to figure it out urls.     
*eg: <a href-"{% url 'addtask' %}">Add a New Task</>* (misspelled = to - in order to avoid an anchor tag)    

To avoid name collisions ,  eg: two urls called index     
We add in the app’s urls.py file, above urlspatterns:    
app_name = "appName"      
*eg: app_name = "tasks"*    
And in the html file:    
{% url ‘appName:addtask’ %}     
*eg: <a href-"{% url 'tasks:addtask' %}">Add a New Task</>*      

#### Forms:  actions.     
The document will react to our interactions,     
in this case, when we submit a New Task, the document will take us back to the form     

#### Forms:  methods     
When we are requesting content, the implicit method associated is GET     
When we are submitting data that can could change the information stored in the application, We are using the POST method.     

#### CSRF token     
{% csrf_token %}     
It is a requirement when we have a form with the post method     
CSRF: Cross Site Request Forgery    
The csrf token changes on each session, so when the users submit that form, the csrf token is submitted too         
Only if the token is valid, the submission is allowed       
This allows to design forms that are not vulnerable to the forgery vulnerability        
(other user submitting their data to other user’s application )

#### Creating forms with Django    
[in views.py]    
We import the forms library    
We create a Python Class  that represents the form       
When we render the html file, we add a Context Dictionary {"key":value} that gives to the template access to the python class we created with all its values (these are the fields in our form)      
[in an html file]     
{{ key }} Django will generate and inject the content in the html file to make the form work.      
 Now, if we want to update the form, we can just update the Python Class and its fields.     

#### Form Validation
We need to include client side validation but also Server Side Validation to be sure that our data is going to be accurate and clean.     
*eg: addTask [function in tasks/views.py]*


#### Redirect Users
After submitting a task, the logical behaviour would be to go back to the index.html and be able to see all the tasks:     
Django makes this process easy,   
Instead of hard code the path, Django will figure it out what is the path to index in the task app
*eg: addTask [function in tasks/views.py]*

#### Sessions
We are storing variables in a Local Variable      
Any person visiting the website will see the same exact list of tasks     
We would like different users to see their personal list of tasks    

Sessions are a way to:    
Make Django remember who you are     
Store data about our particular session     
To store variables, Django uses tables...

This is just to beginning of storing data.    
Django gets very powerful when working with databases     
SQL, Models and migrations: lecture4     

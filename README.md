# django-CS50: DJANGO TUTORIAL

I created these projects following the tutorial     
CS50's Web Programming with Python and JavaScript 2020     
https://www.youtube.com/playlist?list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu    
to understand how Django works.    
Each individual project contains my personal notes taken during the lectures.   
CS50 Lectures:    
Lecture 3 - Django      
Lecture 4 - SQL, Models and Migrations      

#### SET UP
(Create Virtual Environment if necessary)      
Python version: 3.9.2    
Django version: 3.1

What Python version can I use with Django?:    
https://docs.djangoproject.com/en/3.2/faq/install/

[in Terminal]    
Check python version: python    
Check django version: python -m django --version

Link (Django Documentation): https://www.djangoproject.com/

CHANGE THE SECRET KEY in settings.py:      
https://miniwebtool.com/django-secret-key-generator/


#### DJANGO PROJECTS:
A Django Project usually consists in one or more Django Applications.   
Each Application will offer a different service or functionality inside our bigger project.    

### Project: Lecture3
Introduction to Django, this project contains the next applications:

#### Applications:
#### -hello App
It returns a response when we visit *localServer*/hello  
Inside this app, I included the next options:  
*localServer*/hello/ [It renders an html template: index.html]  
*localServer*/hello/cristian [an http response]  
*localServer*/hello/cthulhu  [an http response]  
*localServer*/hello/*AnyName*  [It renders an html template (greet.html) that uses placeholders]  
#### -newyear App
It returns Yes or No depending if the current day is New Year.
*localServer*/newyear
#### -tasks App     
A Task Management App, displays a list of tasks.          
It uses a form to add new tasks.    
It uses Template Inheritance to create continuity through the pages.    
The app includes Client Side Validation & Server Side Validation.    
It uses sessions to personalise what is displayed to each different user.       

### Project: Lecture 4 - Airline
A web project that represents what an airline might want to store in its own web app:    
Airports, flights & passengers
#### Applications:
#### -flights    
This app displays a list of flights,      
Each flight is a link to the specific flight page were we can see more detailed information, including passengers and allows us to include new passengers.      
The tables, where the information is stored, are related between them.       
Django stores the information in a database using SQLite (by default).     
Django makes easy to represent data using models.     
Migration is a process necessary to update and include the created models through Django    
Django Admin: A built-in app designed for the manipulation of the models.       
#### -users     
App that allows us to represent Users
It uses Django's authentication features

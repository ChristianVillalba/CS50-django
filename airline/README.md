# NOTES: Lecture 4:  Airline project
These notes were taken during the lecture:    
*SQL, Models and Migrations - Lecture 4 - CS50's Web Programming with Python and JavaScript 2020*       
Link (YouTube) : https://www.youtube.com/watch?v=YzP164YANAU&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=6&ab_channel=CS50     
The next notes are just references of what I considered useful information related to this project.   
Good written documentation is a key part of Django:   
Link (Django Documentation): https://www.djangoproject.com/

### SQL , Models & Migrations:   
SQL: Database Language     
Models: python's classes and objects    
Migrations: technique to update database   

#### Data:
We will use a relational databases management system (SQL) to store information in a table.      
Tables have rows and columns    
Each column represent a field I want to keep track on     
Each row represents individual flights    
eg: database in web application that a airline can use   

#### SQLite:  relational databases management system
It sores all our data in a single file    
The SQLite syntax (Django's default), can be applied to other SQL databases too
Each piece of data have a type. SQLite types:     
Text, Numeric, Integer, Real,    
BLOB Binary Large Object (images, sounds, videos)   

#### JOINING TABLES:
Sometimes we will need to store information in different tables related between them    
eg: flights, airports , passengers...    
This creates different types of relationships:    
Many to many (multiple passengers can have multiple flights) ,    
many to one (many passengers in a flight) ,    
one to many (one city, many flights) ...   

## DJANGO MODELS:
It's a way to representing data inside a Django Application

#### models.py
This file inside our app defines the models that exist for our application   
Every model is a python class.    
We can think in one model as each of one main table we care about storing information about.     
We use ForeignKey to stablish the relationships between tables,     
Then we can add different arguments.    
We can manipulate SQL just by using python models
Classes represents different types of data
We can interact with those classes and their properties on those with Django, it figures it out the SQL queries , executing these queries and just returning the resulting back to us.

## MIGRATIONS
To actually update the database and include the models we created through Django,     
we will have to make migrations, This is a 2 steps process:    
1) Create the migrations      
Django receive the instructions about how to manipulate the database    
2) Applying those changes to the database    

### Django Admin:
A built-in app designed for the manipulation of the models    
We need to create an administrator account in our Django application    
to be able to manipulate our Flight(s) and Airport(s) from the Admin App    
eg: All the Flights added trough the app will be displayed on the flights app   
We can specify any particular settings that we want to apply to how the admin page is displayed or even add some functionality.

### Users
Authentication: the ability to users to log in & out
Django has authentication features
<!--
## Secret Bonus: SQLite Commands:
[in Terminal sqlite3]

Creating a table:
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL,
)

Inserting Data:
INSERT INTO flights
    (origin, destination, duration)
    VALUES (“London”, “Seoul”, 415)

Retrieve Data:
We retrieve the data without modify it
SELECT * FROM flights;    			*=select all
SELECT origin, destination; FROM flights;
SELECT * FROM flights WHERE id=3; 	all the information about that flight
SELECT * FROM flights WHERE origin = “Paris”;
SELECT * FROM flights WHERE duration > 256 or origin = “London”;
SELECT * FROM flights WHERE origin in (“Toronto”, “Madrid”);
SELECT * FROM flights WHERE origin like “%a%”;     RegEx

Update Data:
Change the data already in our database
UPDATE flights
    SET duration = 512
    WHERE origin = “Madrid”
    AND destination = “Tokyo”;

Delete Data:
DELETE FROM flights WHERE origin = “Madrid”

Functions:
Average, max, min, sum, count, ….

Other Clauses:
Limit, Order by, Group by, Having...

An Association table or Joining Table:
SELECT first_name, origin, destination
FROM flights JOIN passengers
ON passengers.flights_id  = flights.id ;

-->

# WhereCanIEat
As someone who suffers from severe allergies, I am always trying to figure out if I will be able to eat at restaurants around me. Some restaurants have nuts in their kitchens, others are very careful to avoid contamination and others have no nuts at all. Servers at these restaurants also have varying degrees of understanding of what it means to have a severe allergy.

Traditional rating sites will occasionally have reviews that state the good or bad experience a diner with allergies has had, but and these are few and far between. The goal of this website would be to bring together ratings reviews by, and for people with allergies.

## Before you start
Ensure you have Python 2.x.x and Django installed. Once checked out, the application can be run with 
```
python manage.py runserver
```
This will start the development server on port 8000 locally.

## Design Decisions
Django was chosen for this application due to the large number of features that it ships with out of the box. Built in SQL connections and an admin screen allow for data to be easily entered and modified while the UI components are built.

SQLite is currently being used for the database solution. There are two tables used, one to store restaurant information and the other to store reviews of the restaurants. These tables are joined by the unique name field. Within the application, the most often used database query is for all restaurants in a current city.

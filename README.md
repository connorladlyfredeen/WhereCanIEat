# WhereCanIEat
As someone who suffers from severe allergies, I am always trying to figure out if I will be able to eat at restaurants around me. Some restaurants have nuts in their kitchens, others are very careful to avoid contamination and others have no nuts at all. Servers at these restaurants also have varying degrees of understanding of what it means to have a severe allergy.

Traditional rating sites will occasionally have reviews that state the good or bad experience a diner with allergies has had, but and these are few and far between. The goal of this website would be to bring together ratings reviews by, and for people with allergies.

## Before you start
Ensure you have Python 2.x.x and Django installed. Once checked out, the application can be run with 
```
python manage.py runserver
```
This will start the development server on port 8000 locally. More info can be found here: https://www.djangoproject.com/start/.
Once started, the home page can be reached at /reviews and the admin page can be reached at /admin. An admin profile can be created with the following command:
```
python manage.py createsuperuser
```

## Design Decisions
Django was chosen for this application due to the large number of features that it ships with out of the box. Built in SQL connections and an admin screen allow for data to be easily entered and modified while the UI components are built.

SQLite is currently being used for the database solution. There are two tables used, one to store restaurant information and the other to store reviews of the restaurants. These tables are joined by the unique name field. Within the application, the most often used database query is for all restaurants in a current city.

The ultimate goal would be to transfer this to MongoDB. This would require some code changes but would ultimately simplify the data model. While right now we require two tables joined by a common name, we could simplify this to be a single document for each restaurant that has been reviewed. It would have the following format:
```
{
  name: String,
  city_name: String,
  food_type: String,
  reviews: {[
    {
      reviewer_name: String,
      comment: String,
      stars: Int
    }
  ]}
}
```
The code would also have to be adjusted in the settings.py and models.py files to use the MongoDB Django driver and to amalgamate the two models for comment and restaurant together.  (See here for documentation: https://django-mongodb-engine.readthedocs.io/en/latest/)

## Current Features

## Challenges
Timing was very tight for me on this project, so I had to decide what the most important features where that could be built in the given time. In the end, I decided that the most important thing to have was to be able to see which restaurants where reviewed near you based on searching for your city. This is the core of the service and therefore the most important piece to show its value.

## Future Features
Beyond simple cosmetic improvements, these are the features that I would implement if I had unlimited time.
```
1. Web scraping and external apis to pull in existing reviews and data on restaurants as it relates to allergies.
2. Improved search ability to enable users to search by their location not only city and to search byt food type, price range, star ranking, allergy accessibility ranking etc.
3. Duplication and false data chacking using some sort of captcha or account feature
4. Ability to let users flag bad reviews for moderation
5. Build out pages for each restaurant
```

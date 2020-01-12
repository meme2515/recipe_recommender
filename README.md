# Recipe Recommender 🍴
Cross-platform mobile fridge manager and recipe recommender based on Flutter and Python.

## Backend

### Database (SQLite) 💾

1. [Database design](https://ondras.zarovi.cz/sql/demo/)

![img](database_design.JPG)

### Flask Setup 🌶️

1. [Codementor's Flask guide](https://www.codementor.io/@dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx)
2. [Grinberg's Flask guide (Crash Course)](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask?fbclid=IwAR10kkkJNCcgVAIHkaDZKdXq3yL1lP8kGykt3466kT61olZmhvz6wjoBiNY)
3. [Grinberg's Flask guide (Mega Tutorial)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

Resources will use HTTP methods as follows:

| HTTP Method | URI                                                           | Action                                                  |
|-------------|---------------------------------------------------------------|---------------------------------------------------------|
| GET         | http://[hostname]/recommender/ingredients/[ingredient_id]     | Retrieve an ingredient                                  |
| GET         | http://[hostname]/recommender/ingredients/search/[search_key] | Retrieve list of ingredients that begin with search key |
| GET         | http://[hostname]/recommender/ingredients/user/[user_id]      | Retrieve list of ingredients that the user has          |

### Sample Recipes


## Frontend

### Flutter

## Miscellaneous

### Web Scraping

<h1 align="center">RESTful API for Udacity casting agency :mega:</h1>
<p>
  <img src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/wanderindev/udacity-casting-agency/blob/master/README.md">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/wanderindev/udacity-casting-agency/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://htmlpreview.github.io/?https://github.com/wanderindev/udacity-casting-agency/blob/master/htmlcov/index.html">
    <img alt="Coverage" src="https://img.shields.io/badge/coverage-97%25-yellowgreen.svg" target="_blank" />
  </a>  
  <a href="https://github.com/wanderindev/udacity-casting-agency/blob/master/LICENSE.md">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/JavierFeliuA">
    <img alt="Twitter: JavierFeliuA" src="https://img.shields.io/twitter/follow/JavierFeliuA.svg?style=social" target="_blank" />
  </a>
</p>

>Udacity Casting Agency API is the capstone project for the 2019 Udacity Full-stack Developer Nanodegree. Unlike
>other projects in the nanodegree, this one does not have starter code, just a general specification and
>a grading rubric.

## About
The project provides a RESTful API for performing CRUD operations for models stored in a Postgresql database.

The database consists of three tables: ```actors```, ```movies```, and ```movies_actors```.  

The first two tables store the actor model and movie model.
The third table is use for modeling the many-to-many relationship between actors and movies.

A Postman collection and two Postman environment are provided to test all endpoint locally and at Heroku.

The API allows for the following users with different roles and permissions to authenticate and call the endpoints:

| Users                         | Role      | Permissions                                                                       |
|-------------------------------|-----------|-----------------------------------------------------------------------------------|
| assistant@udacity-casting.com | assistant | get:actor, get:actors, get:movie, get:movies                                      |
| director@udacity-casting.com  | director  | all assistant permissions plus post:actor, patch:actor, delete:actor, patch:movie |
| producer@udacity-casting.com  | producer  | all director permissions plus post:movie, delete:movie                            |

The included Postman collection and UnitTest are setup to call the [Auth0](https://auth0.com/) endpoint to retrieve a valid token so it is not necessary to
setup authentication prior to testing the project.

The project is deployed to Heroku at [Udacity-Casting-Agency](https://shielded-journey-52543.herokuapp.com).  Instructions on
how to test the deployed API with Postman are provided below.

## Install
To use the project in your development machine, clone it, and go to the project's root:
```sh
git clone https://github.com/wanderindev/udacity-casting-agency.git
cd udacity-casting-agency
``` 
From the project's root, create and activate your virtual environment:
```sh
cd udacity-casting-agency
python3 -m venv venv
. venv/bin/activate
```

And install the project's dependencies:
```sh
pip install -r requirements.txt
```

## Development
Edit the code as required.  Here is the list of the most important modules and packages in the project:

* ```app.py``` contains the app factory.
 * ```auth.py``` contains the authentication/authorization code.
* ```config.py``` contains the app settings.
* ```manage.py``` contains the database migration code.
* ```run.py``` runs the application.
* ```/models``` contains the modules for the database models.
* ```/resources``` contains the modules with the API endpoints.
* ```/tests``` contains the modules with the UnitTests.

### Database
To test your code modifications you need to have a PostgreSQL instance running locally. 

I included a Dockerfile and a docker-compose.yml that runs a local PostgreSQL instance and
creates two databases (one for development and one for testing).

If you have Docker installed and configured in your system, this is the 
recommended way for running the database.  Otherwise, create and initialize 
the databases in your own PostgreSQL instance and adjust
the connection string in ```config.py```.

To use the included PostgreSQL setup, **open a new terminal window**, go into the ```postgresql``` directory, 
and run docker-compose:
```sh
cd udacity-casting-agency/postgresql
docker-compose up --build
```

### API
Once your database is running in its own terminal window, you can run the API from **the terminal window where your virtual environment is activated**:
```sh
export FLASK_APP=run
flask run
```

### Tests
To insure code quality, I added UnitTest to the project. All tests all located in the tests package.

To test the project, **from the terminal window where your virtual environment is activated** run:
```sh
coverage run -m unittest tests/test_actor_model.py tests/test_movie_model.py tests/test_actor_resources.py tests/test_movie_resources.py tests/test_errors.py
```
The included tests provide 97% coverage for the codebase. You can find the coverage report [here](https://htmlpreview.github.io/?https://github.com/wanderindev/udacity-casting-agency/blob/master/htmlcov/index.html).

### Postman
Open Postman and import the included collection (```udacity-casting.postman_collection.json```)
and the two included environments (```udacity-casting-local.postman_environment.json``` and ```udacity-casting-heroku.postman_environment.json```).

#### Run Postman collection locally
With the API running in a terminal window and the database running in another terminal window, from Postman:

1. Click on ```Runner```. 
2. Select the ```udacity-casting``` collection, and the ```udacity-casting-local``` environment.
3. Scroll down and click on ```Run Udacity-Casting```.

#### Run Postman collection at Heroku
The API is running at https://shielded-journey-52543.herokuapp.com.  To test the remote API, from Postman:
1. Click on ```Runner```.
2. Select the ```udacity-casting``` collection and the ```udacity-casting-heroku``` environment.
3. Scroll down and click on ```Run Udacity-Casting```.

 ## Author

👤 **Javier Feliu**

* Twitter: [@JavierFeliuA](https://twitter.com/JavierFeliuA)
* Github: [@wanderindev](https://github.com/wanderindev)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Javier Feliu](https://github.com/wanderindev).<br />

This project is [MIT](https://github.com/wanderindev/udacity-casting-agency/blob/master/LICENSE.md) licensed.

***
_I based this README on a template generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
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

## Project overview
The project provides a RESTful API for performing CRUD operations for models stored in a Postgresql database.
The database consists of three tables: actors, movies, and movies_actors.  The first two tables store the actor model and movie model.
The third table is use for modeling the many-to-many relationship between actors and movies.

The API allows for three users with different roles and permissions to authenticate and call the endpoints.

The project is deployed to Heroku.

A Postman collection and two Postman environment are provided to test all endpoint locally and at Heroku.

Unittests are provided to test all endpoint succeess and failure states.

## How to use

### Clone the repository
Clone the repository and cd into the project root:
```sh
git clone https://github.com/wanderindev/udacity-casting-agency.git
cd udacity-casting-agency
``` 

### The database
I included a Dockerfile and a docker-compose.yml that runs a local Postgresql instance and
creates two databases (one for development and one for testing).

If you have Docker installed and configured in your system, this is the 
recommended way for running the database.  Otherwise, create and initialize 
the databases in your own Postgresql instance and adjust
the connection string in ```config.py```.

To use the included Postgresql setup, cd into the postgresql directory 
and run docker-compose:
```sh
cd postgresql
docker-compose up --build
```

### The backend
In a second terminal window, cd into the project root, create a virtual
environment, and activate it:
```sh
cd udacity-casting-agency
python3 -m venv venv
. venv/bin/activate
```
Install the project requirements:
```sh
pip install -r requirements.txt
```

To run the tests, use:
```sh
coverage run -m unittest tests/test_actor_model.py tests/test_movie_model.py tests/test_actor_resources.py tests/test_movie_resources.py tests/test_errors.py
```

To run the RESTful API, use:
```sh
export FLASK_APP=run
flask run
```

### Postman
Open Postman and import the included collection (```udacity-casting.postman_collection.json```)
and the two included environments (```udacity-casting-local.postman_environment.json``` and ```udacity-casting-heroku.postman_environment.json```).

#### Run Postman collection locally
With the API running in the terminal window, click on ```Runner``` in Postman, select the ```udacity-casting``` collection and the 
```udacity-casting-local``` environment.  Scroll down and click on ```Run Udacity-Casting```.

#### Run Postman collection at Heroku
The API is running at https://shielded-journey-52543.herokuapp.com.  To test the remote API, click on ```Runner``` in Postman, select the ```udacity-casting``` collection and the 
```udacity-casting-heroku``` environment.  Scroll down and click on ```Run Udacity-Casting```.

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
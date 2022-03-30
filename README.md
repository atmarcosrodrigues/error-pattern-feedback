# Error Patterns Feedback [![Build Status](https://travis-ci.org/atmarcosrodrigues/errorpatternfeedback-v2.svg?branch=master)](https://travis-ci.org/atmarcosrodrigues/errorpatternfeedback-v2)


The difficulty that students face in learning programming, both because of motivational aspects such as the ability to master the new skills learned is a common problem in introductory programming courses. The literature in the area shows us that the use of corrective feedback is one of the main methodologies used to assist students in this learning process. However, provide personalized accompaniment that meets the needs of each student, as well as,understanding the real problems faced by them is a great challenge for teachers.

In this context, we propose a detailed study of the error patterns detected in an introductory programming class at the Federal University of Campina Grande. The objective of this approach is to identify classes/types of errors and propose
a detailed taxonomy to represent these patterns, considering specific errors not covered in the literature and making a direct connection to feedback and materials instructional.

This project provides a server where professors and monitors of programming disciplines can provide questions to students and provide institutional feedback in order to identify error patterns and determine which types of errors are most common in introductory programming courses.



## Technologies used

* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[PostgreSQL](https://www.postgresql.org/download/)** – Postgres database offers many [advantages](https://www.postgresql.org/about/advantages/) over others.
* Minor dependencies can be found in the requirements.txt file on the root folder.

## Installation / Usage

* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed virtualenv globally as well. If not, run this:

    ```bash
    pip install virtualenv
    ```

* Git clone this repo

    ```bash
    git clone git@github.com:
    ```

* ### Dependencies

    1. Cd into your the cloned repo:

        ```bash
        cd feedback-error-patterns
        ```

    2. Create and get into your virtual environment:

        ```bash
        virtualenv -p python3 venv
        source venv/bin/activate
        ```

    3. Environment Variables

        Install python-dotenv [Dotenv](https://pypi.org/project/python-dotenv/) (The package are in requirements.txt)

        ```bash
        pip install python-dotenv
        ```

        Create a .env file and add the following:

        ```bash
        POSTGRES_URL="YOUR_POSTGRES_URL:PORT"
        POSTGRES_USER="YOUR_POSTGRES_USER"
        POSTGRES_PW="YOUR_POSTGRES_PASSWORD"
        POSTGRES_DB="YOUR_POSTGRES_DATABASE"
        POSTGRES_DB_TEST="YOUR_POSTGRES_DATABASE_FOR_TESTS"
        SECRET_KEY="YOUR_GENERATED_STRING_RANDOM_CHARACTERS"

        FLASK_APP="run.py"
        APP_SETTINGS="development"
        ```

        Dotenv will load your environment variables by reading the key-value pairs from the .env file.


    4. Install the requirements
    
        ```bash
        (venv)$ pip install -r requirements.txt
        ```

* ### Database Migrations

    Make sure your postgresql server is running. Then, on your psql console, create your database: (In this example: error_patterns use your own database name)

    ```bash
    $ psql -U postgres
    > CREATE DATABASE error_patterns;
    ```

    In the project directory, make and apply your Migrations

    ```bash
    (venv)$ flask db init

    (venv)$ flask db migrate
    ```

    And finally, migrate to persist them on the database

    ```bash
    (venv)$ flask db upgrade
    ```

* ### Running the Server

    On your terminal, run the server using this one simple command:

    ```bash
    (venv)$ flask run
    ```

    You can now access the app on your local browser by using

    ```bash
    http://localhost:5000
    ```
* ### Running Tests

    On your terminal run:

    ```bash
    (venv)$ python -m unittest discover -p '*test*'
    ```


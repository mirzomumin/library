# Library of books
A Django application that provides all books and searching a specific one through title and author name.
It also allows update author name, category name and book info.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/mirzomumin/library.git
$ cd library
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/swagger/`.


## Database

To create database of the project run the following command:
```sh
(env)$ python manage.py migrate
```
the primary database settings of django are configured for sqlite3 but
you can set any database you wish

## Fixtures

To fill database in data for Author, Category and Book run the commands:
```sh
(env)$ python manage.py loaddata apps/book/fixtures/authors.json --app book.author
(env)$ python manage.py loaddata apps/book/fixtures/categories.json --app book.category
(env)$ python manage.py loaddata apps/book/fixtures/books.json --app book.book
```

Once you've done you can move again to `http://127.0.0.1:8000/swagger/` to check data.


## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test
```

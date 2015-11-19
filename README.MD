Overview:
-------------------------

This project is used to demonstrate SQL Injection works.
To demonstrate SQL Injection, we do not use the python API, instead we generate our SQL Statement by placeholders.
To defense against SQL Injection, we can USE python API, instead of the first method.
Both two functions are implmented under model.py.

Installation instructions
-------------------------

### Prerequisites

Required:

* python 2.7
* web.py lib
* MySQL

## web.py
To install web.py, you simply can use easy_install or pip to install it

## MySQL
You need to have a user `CS8083` with password `CS8083`, under it, Database `CS8083` should be created.
And a table called `USER` should be created, you can check the schema in schema.sql

### Build

To build ChronoSync from the source:
    python userInfo.py
# Report Exporting Service

## Introduction

The goal of this exercise is to see:

1. What your "production" level code looks like (OO, Documentation, etc)

2. How you ensure that the code actually works as expected (Testing)

3. How you respond to tight deadlines (Which shortcuts you take)

4. Your approach and creativity to crafting a solution


## The Task

The goal is to implement the Report Exporting Service. The purpose of this service is to take abstract reports and generate PDF documents and XML files out of them.

Services within the system are stand-alone (flask) python applications with a thin layer of (RESTful) web services as the interface.

We have two abstract reports made available to you on a PostgreSQL server located at:

postgres: horton.elephantsql.com

You can find all of this information in the [config.py](https://github.com/STiago/report-exporting-service/blob/master/app/config.py) document.

A wireframe of a potential PDF template is attached at the bottom of this document.


## Expectations

1. Define and implement web API endpoints for generating and returning PDF and XML reports given a report_id.

2. Create reusable templates for exporting to PDF. (For XML just do a direct transform)


## Solution

The purpose of this service is to take abstract reports and generate PDF documents and XML files out of them.

How to run the service: ./app/app.py
How to run the tests: ./app/tests.py

Before running this service or its tests:

  - Ensure you have installed the following packages: libffi-dev, wkhtmltopdf, python-dev, python2.7, virtualenv, python-virtualenv

  - In the direcoty report-exporting-service, execute the following commands: virtualenv env; env/bin/pip install -r requirements.txt

  - Set up the database information (based on PostgreSQL) for the different environments in: ./app/config.py

  - Please note that the test database must contain some example reports in order to run the test sucessfully

Endpoints:

- http://localhost:8080/report/<id>/pdf -> Generates the pdf report for a given report id 
- http://localhost:8080/report/<id>/xml -> Generates the xml report for a given report id

We have here some examples of the solution:

![Image1]()

![Image2]()

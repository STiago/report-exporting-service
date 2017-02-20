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

You can find all of this information in the [config.py]() document.

A wireframe of a potential PDF template is attached at the bottom of this document.


## Expectations

1. Define and implement web API endpoints for generating and returning PDF and XML reports given a report_id.

2. Create reusable templates for exporting to PDF. (For XML just do a direct transform)


## Solution

We have here some examples of the solution:

![Image1]()

![Image2]()

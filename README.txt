
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



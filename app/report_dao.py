#!env/bin/python
from __future__ import with_statement
from contextlib import contextmanager
import psycopg2
import psycopg2.pool
import json
from flask import current_app

pool = None

# Create pool with min number of connections of 1, max of 10
def get_connection_pool():
    global pool
    if pool == None:
        dbName = current_app.config.get("DATABASE_NAME")
        dbUser = current_app.config.get("DATABASE_USER")
        dbHost = current_app.config.get("DATABASE_HOST")
        dbPass = current_app.config.get("DATABASE_PASSWORD")
        CONNECTION_STRING = "dbname='%s' user='%s' host='%s' password=%s" % (dbName, dbUser, dbHost, dbPass)
        pool = psycopg2.pool.SimpleConnectionPool(1,10, CONNECTION_STRING)
    return pool

@contextmanager
def get_cursor():
    pool = get_connection_pool()
    con = pool.getconn()
    try:
        yield con.cursor()
    finally:
        pool.putconn(con)

def get_report_data(report_id):
    with get_cursor() as cursor:
        cursor.execute('SELECT * FROM reports WHERE id = %s', [report_id])
        row = cursor.fetchone()
        toReturn = None
        if row != None:
            try:
                toReturn = json.loads(row[1])
            except Exception:
                print "Cannot deserialize the report data"

        return toReturn

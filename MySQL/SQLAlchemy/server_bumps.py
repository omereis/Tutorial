import asyncio
import getopt, sys
from time import sleep
import datetime
import json, os
from sqlalchemy import create_engine, MetaData

database_engine = None
connection = None

try:
    database_engine = create_engine('mysql+pymysql://bumps:bumps_dba@NCNR-R9nano.campus.nist.gov:3306/bumps_db')
    connection = database_engine.connect()
    print("Database connected")
except Exception as e:
    print("Error while connecting to database bumps_db in NCNR-R9nano.campus.nist.gov:3306:")
    print("{}".format(e))
    exit(1)
finally:
    if connection:
        connection.close()
        print("Database connection closed")
    else:
        print("Fatal error. Aborting :-(")
        exit(1)
print("Connection successful")
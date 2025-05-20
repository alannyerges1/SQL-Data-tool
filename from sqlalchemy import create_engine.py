from sqlalchemy import create_engine
import pyodbc 
import pandas as pd
import os

#Get password from Env Var
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
#SQL DB details
driver = "{SQL Server Native Client 11.0}"
server = "haq-PC"
database = "AdventureWorksDW2019;"


#Extract data from SQL Server
def extract():
    try:
        src_conn = pyodbc.connect('Driver=' + driver + ';SERVER=' + server + '\SQLEXPRESS' + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd) 

import cx_Oracle
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

load_dotenv()

DBUSER = os.environ.get('DBUSER')
DBPASSWORD = os.environ.get('DBPASSWORD')
DBHOST = os.environ.get('DBHOST')
DBSERVICE = os.environ.get('DBSERVICE')

def saveToDatabase(data):
    connection = connect(
    host=DBHOST,
    user=DBUSER,
    password=DBPASSWORD,
    database=DBSERVICE)\


    cursor = connection.cursor()

    insert_clients_query = """
    INSERT INTO CLIENTS
    (name, phone, email, adress, latlng, salary, age, devise, achat, vente, country, flag)
    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
     """
    for item in data:
        #print(f"connexion 2 : {connection}")
        #print(list(item.values()))
        client = list(item.values())
        #print(f"connexion 3 : {connection}")
        cursor.execute(insert_clients_query, client)


    #print(f"connexion 4 : {connection}")
    connection.commit()
    connection.close()
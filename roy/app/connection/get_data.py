import pandas as pd
import pyodbc
from decouple import config

server = config('SERVER_AZ')
database = config('DATABASE_AZ')
username = config('USERNAME_AZ')
password = config('PASSWORD_AZ')
driver = '{ODBC Driver 18 for SQL Server}'

def get_data(query):
    cnxn = None
    cursor = None
    df = None
    try:
        cnxn = pyodbc.connect('DRIVER=' + driver + 
                        ';SERVER=' + server + 
                        ';DATABASE=' + database + 
                        ';UID=' + username + 
                        ';PWD=' + password)
        cursor = cnxn.cursor()
        print('Connection established')
        df = pd.read_sql_query(query, cnxn)
        return df
    except Exception as e:
        print('Cannot connect to SQL server', e)
    finally:
        if cursor:
            cursor.close()
        if cnxn:
            cnxn.close()
    return df

# Ejemplo de consulta sobre la tabla de monthly REPORT
df = get_data('SELECT * FROM [monthly_report]')

print(df)


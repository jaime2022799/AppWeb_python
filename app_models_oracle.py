import cx_Oracle 
from datetime import date
from flask import Flask , render_template ,  jsonify , request 


try:
    connection=cx_Oracle.connect(
        user='user_boss',
        password='2024',
        dsn='localhost:1521/ORCL',
        encoding='UTF-8'

    )
    print(connection.version)



except Exception as ex:
    print(ex)
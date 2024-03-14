from flask import Flask, render_template , request ,jsonify , redirect, url_for
import cx_Oracle 
import requests
from datetime import date , datetime 

app = Flask(__name__)

try:
    connection=cx_Oracle.connect(
        user='user_boss',
        password='2024',
        dsn='localhost:1521/ORCL',
        encoding='UTF-8'

    )
except Exception as ex:
    print(ex)


@app.route('/')

@app.route('/index.html')
def home():
    return render_template('/index.html')


cursor = connection.cursor()


@app.route('/index', methods=['POST'])
def pag_formulario_administrativo():
     #VARIABLES
    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")


    if request.method == 'POST':

        
        email = request.form['email']

        execute = """
         call email_formulario_administrativo ('email':email)
        """

        cursor.execute(execute, {'email':email})

        connection.commit()


    else:
        return "404  ERROR REQUEST", 400
     
    return render_template('/login.html') , 200



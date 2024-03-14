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

@app.route('/login.html')
def signup():
    return render_template('/login.html')


cursor = connection.cursor()



@app.route('/login.html', methods=['POST'])
def post_data():

    #VARIABLES
    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")
   

    if request.method == 'POST':

       
        email = request.form['email']

        execute = """
            call email_signup_3 ('email':email)
        """
        
        cursor.execute(execute, {'email':email})
                       
       
        connection.commit()
        
        
    else:
        return 'BAD REQUEST', 400
    
    return render_template('/login.html'), 200


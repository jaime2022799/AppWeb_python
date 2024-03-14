import cx_Oracle , conexion_oracle 
from datetime import date
from flask import Flask , render_template ,  jsonify , request , redirect, url_for

app = Flask(__name__)

@app.route('/login')
def pag_signup():
    return render_template('/login.html')


@app.route('/index.html')
def pag_index():
    return render_template('/index.html')


try:
    connection=cx_Oracle.connect(
        user='user_boss',
        password='2024',
        dsn='localhost:1521/ORCL',
        encoding='UTF-8'

    )
    

    
except Exception as ex:
    print(ex)




@app.route('/login.html', methods=["POST"])

def pag_signup_registro():
    
    #coneccion a oracle con cursor 
        cursor=connection.cursor()
        
        #variables name del html signup
        
        global id_signup
        id_signup = int

        fecha = date.today()
        
          
    #llamamos al request del metodo post 
        if request.method == "POST":
            nombre_registro = request.form['nombre']
            apellido_registro = request.form['apellido']
            email_registro = request.form['email']
            password__registro = request.form['password_create']
            password_registro_confirm = request.form['password_confirm']

            call_sp_signup = '''
            INSERT INTO SIGNUP (ID_SIGNUP,EMAIL,CLAVE_NUEVA,CLAVE,NOMBRE,APELLIDO,FECHA) VALUES (29,'GIUSEPE@GMAIL.COM','GIUSEPE2024','GIUSEPE2024','GIUSEPE','GIUSEPE','21-01-2024')
            '''
            cursor.execute(call_sp_signup)
            connection.commit()
            return render_template('/login.html')
        #return render_template('/index.html')
        #return redirect(url_for('/home'))
        else:
            return "404 request"


@app.route('/login.html', methods=["POST"])

def pag_login_acceso():
     
     cursor=connection.cursor()

     id_login = int

     fecha = date.today()
    

     if request.method == 'POST':
          email_login = request.form['email']
          clave_login = request.form['password']

          call_login_acceso = '''
           INSERT INTO LOGIN (ID_LOGIN,EMAIL,CLAVE,SIGNUP_ID,FECHA) VALUES (12,'GIUSEPE@GMAIL.COM','GIUSEPE2024','28','21-01-2024')
          '''
          cursor.execute(call_login_acceso)
          connection.commit()
          render_template('/index.html')
     else:
          return "404 request"
     
     return



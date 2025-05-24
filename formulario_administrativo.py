import cx_Oracle , signup_registro 
from flask import Flask , render_template ,  jsonify , request , redirect, url_for

id_signup = signup_registro.id_signup

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

@app.route('/index.html')
def pag_index_formulario():
    return render_template('/index.html')


@app.route('/index',methods=["POST"])

def pag_formulario_administrativo():
     cursor=connection.cursor()

     nombre = request.form['nombre']
     apellido = request.form['apellido']
     tipo_evento = request.form['tipo_evento']
     contacto = request.form['Contacto']
     direccion = request.form['direccion']

     if request.method == 'POST':
        call_sp_signup = f'call  INSERTAR_REGISTRO_FORMULARIO_ADMINISTRATIVO ({id_signup},{nombre},{apellido},{tipo_evento},{contacto},{direccion})'
            
        cursor.execute(call_sp_signup) 

        return render_template('/index.html')   

     else:
         return "404  ERROR REQUEST"
     
     return "404 ERROR "
from flask import Flask, render_template , request ,jsonify , redirect, url_for
import cx_Oracle 
from datetime import date , datetime 
from werkzeug.utils import secure_filename
import requests
import json

#import conexion_oracle 

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


@app.route('/index.html')
def home():
    return render_template('/index.html')


cursor = connection.cursor()



@app.route('/login.html', methods=['POST'])
def post_data():

    #VARIABLES
    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")
   

    if request.method == 'POST':

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password_create = request.form['password_create']
        password_confirm = request.form['password_confirm']


        execute = """
        INSERT INTO SIGNUP (EMAIL,CLAVE_NUEVA,CLAVE,FECHA,NOMBRE,APELLIDO,HORA) 
        VALUES (:email,:password_create,:password_confirm,:fecha,:nombre,:apellido,:time)
        """
        
        cursor.execute(execute, {'email':email, 'password_create':password_create, 'password_confirm':password_confirm, 'fecha':fecha, 'nombre':nombre, 'apellido':apellido, 'time':time})
       
        connection.commit()
        
        
    else:
        return 'BAD REQUEST', 400
    
    return render_template('/login.html'), 200


    
cur = connection.cursor()
cur.execute("SELECT * FROM SIGNUP WHERE HORA IS NOT NULL")
for id_signup , email, clave_nueva , clave,fecha,nombre,apellido,hora in cur:
    print("Campo: ", id_signup)
    print("Campo: ", email)
    print("Campo: ", clave_nueva)
    print("Campo: ", clave)
    print("Campo: ", fecha)
    print("Campo: ", nombre)
    print("Campo: ", apellido)
    print("Campo: ", hora)


#definimos la ruta de index para el registro de la cuenta creada pero en el login
@app.route('/index.html', methods=["POST"])
def login_registro():

    #VARIABLES
    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")

    if request.method == "POST":
        email = request.form['email']
        clave = request.form['clave']
       

        execute = """
        INSERT INTO LOGIN (EMAIL,CLAVE,FECHA,HORA) 
        VALUES (:email,:clave,:fecha,:time)
        """
        
        cursor.execute(execute, {'email':email, 'clave':clave,'fecha':fecha,'time':time})
       
        connection.commit()
       
        
        #return render_template('/index.html')
        #return redirect(url_for('/home'))
    else:
        return "404 request", 400
    
    return render_template('/index.html'), 200
    


@app.route('/index', methods=['POST'])
def pag_formulario_administrativo():
     #VARIABLES
    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")


    if request.method == 'POST':

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        tipo_evento = request.form['tipo_evento']
        contacto = request.form['contacto']
        direccion = request.form['direccion']
        email = request.form['email']

        execute = """
        INSERT INTO FORMULARIO_ADMINISTRATIVO (nombre,apellido,tipo_evento,contacto,direccion,email,fecha,hora) 
        VALUES (:nombre,:apellido,:tipo_evento,:contacto,:direccion,:email,:fecha,:time)
        """

        cursor.execute(execute, {'nombre':nombre,'apellido':apellido,'tipo_evento':tipo_evento,'contacto':contacto,'direccion':direccion,'email':email,'fecha':fecha,'time':time})

        connection.commit()


    else:
        return "404  ERROR REQUEST", 400
     
    return render_template('/login.html') , 200




@app.route('/upload', methods=["POST"])
def pag_cotizacion():

     #VARIABLES
    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")
    nombre = 'Cotizacion2024'

    if request.method == 'POST':

        archivo = request.files['archivo']
        archivo_data = archivo.read()
        archivo_nombre = secure_filename(archivo.filename)

        execute = """
            INSERT INTO archivo_bfile_cotizador (nombre,fecha,hora,archivo)
            VALUES (:nombre,:fecha,:hora, :archivo_data))
        """

        cursor.execute(execute, {'nombre':nombre,'fecha':fecha,'time':time,'archivo_data':archivo_data})

        connection.commit()      
    else:
        return "404 ERROR REQUEST", 400
    
    return  render_template('/index.html'), 200


#@app.route('/pago_registro', method='POST')
#def pag_registro_pago():
     #VARIABLES
#    fecha = date.today()
#    fechaHora = datetime.now()
#    time = fechaHora.strftime("%H:%M:%S")

#    if request.method == 'POST':
         
         # rut = request.form['rut']
         # numero_cuenta = request.form['cuenta']
         # nombre_titular = request.form['nombre_titular']
         # cvc_titular = request.form['cvc_titular']
         
        #execute = """
        #    INSERT INTO PAGO_COTIZACION (rut,numero_cuenta,nombre_titular,cvc_titular,fecha,hora) 
            # VALUES (:rut,:numero_cuenta,:nombre_titular,:cvc_titular,:fecha,:hora)       
        #"""
        # cursor.execute(execute, {'rut':rut,'numero_cuenta':numero_cuenta,'nombre_titular':nombre_titular,'cvc_titular':cvc_titular,'fecha':fecha,'hora':hora})
#        connection.commit()  

#    else:
#        return "404 ERROR REQUEST", 400
    
#    return render_template('/login.html'), 200


#@app.route('/registro_titular', method='POST')
#def pag_registro_pago():
     #VARIABLES
#    fecha = date.today()
#    fechaHora = datetime.now()
#    time = fechaHora.strftime("%H:%M:%S")

#    if request.method == 'POST':
         
         # rut = request.form['rut']
         # nombre_titular = request.form['nombre_titular']
         # apellido_titular = request.form['apellido_titular']
         # email_titular = request.form['email_titular']
        #  metodo_de_pago = request.form['metodo_de_pago']
        #  nombre_banco_tarjeta = request.form['metodo_de_pago']
         
        #execute = """
        #    INSERT INTO PAGO_COTIZACION (rut,numero_cuenta,nombre_titular,cvc_titular,fecha,hora) 
            # VALUES (:rut,:nombre_titular,:apellido_titular,:email_titular,:metodo_de_pago,:fecha,:hora,:nombre_banco_tarjeta)       
        #"""
        # cursor.execute(execute, {'rut':rut,'nombre_titular':nombre_titular,'apellido_titular':apellido_titular,'email_titular':email_titular,'metodo_de_pago':metodo_de_pago,'fecha':fecha,'hora':hora,'nombre_banco_tarjeta':nombre_banco_tarjeta})
#        connection.commit()  
        
#    else:
#        return "404 ERROR REQUEST", 400
    
#    return render_template('/login.html'), 200



if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port=5000)
    
   

    

    



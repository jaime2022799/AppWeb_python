from flask import flash,make_response ,  request , render_template
from datetime import date , datetime 
import cx_Oracle 
from werkzeug.utils import secure_filename
from fileinput import filename 
import os
import requests
from app import app, cursor
import app_models_oracle

app.config["UPLOAD_FOLDER"] = "static/uploads"
ALLOWED_EXTENSIONS = set(['pdf','xlsx','txt','csv'])

#definimos la ruta de index para el registro de la cuenta creada pero en el login

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
       
        app_models_oracle.connection.commit()
       
        
        #return render_template('/index.html')
        #return redirect(url_for('/home'))
    else:
        return "404 request", 400
    
def signup_registro():

     #VARIABLES
    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")

    if request.method == "POST":

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
        
        app_models_oracle.connection.commit()
            
            
    else:
        return 'BAD REQUEST', 400
    
def formulario_registro():

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
        INSERT INTO formulario_administrativo (nombre,apellido,tipo_evento,contacto,direccion,email,fecha,hora) 
        VALUES (:nombre,:apellido,:tipo_evento,:contacto,:direccion,:email,:fecha,:time)
        """

        cursor.execute(execute, {'nombre':nombre,'apellido':apellido,'tipo_evento':tipo_evento,'contacto':contacto,'direccion':direccion,'email':email,'fecha':fecha,'time':time})

        app_models_oracle.connection.commit()


    else:
        return "404  ERROR REQUEST", 400



def allowed_file(file):
    file = file.split('.')
    print(file)
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False
    

def registro_archivo():

    
    if request.method == "POST":

        #VARIABLES
        fecha = date.today()
        fechaHora = datetime.now()
        time = fechaHora.strftime("%H:%M:%S")
        nombre = 'Cotizacion_2024'
        
        file = request.files["archivo"]
        print(file)
        filename = secure_filename(file.filename)
        print(filename)
        if file and allowed_file(filename):
            print('permitido')
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        
        execute = """
            INSERT INTO ARCHIVO_COTIZADOR (nombre,fecha,hora,archivo)
            VALUES (:nombre,:fecha,:time,:filename)
        """ 
        cursor.execute(execute, {'nombre':nombre,'fecha':fecha,'time':time,'filename':filename})

        app_models_oracle.connection.commit() 



def registro_pago():

    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")

    if request.method == 'POST':

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        usuario = request.form['usuario']
        email = request.form['email']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        pais = request.form['pais']
        estado = request.form['estado']
        codigo = request.form['codigo']    
        metodo = request.form['paymentMethod'] 
        numeroTarjeta = request.form['numeroTarjeta']   
        nombreTarjeta = request.form['nombreTarjeta']
        expiracion = request.form['expiracion']
        cvv = request.form['cvv']
        #cursor.execute("INSERT INTO DATOS_FACTURA (usuario,email,direccion,telefono,fecha,hora,nombre,apellido) VALUES ('jaime','jaimeretamal@gmail.com','joaquin palacios 556','990383265','14/07/24','15:30','USER_BOSS_100','USER_BOSS_100')")
        execute = """
        INSERT INTO DATOS_FACTURA (usuario,email,direccion,telefono,fecha,hora,nombre,apellido,pais,estado,codigo,metodo,numeroTarjeta,nombreTarjeta,expiracion,cvv) 
        VALUES (:usuario,:email,:direccion,:telefono,:fecha,:time,:nombre,:apellido,:pais,:estado,:codigo,:metodo,:numeroTarjeta,:nombreTarjeta,:expiracion,:cvv)
        """ 
        cursor.execute(execute, {'usuario':usuario,'email':email,'direccion':direccion,'telefono':telefono,'fecha':fecha,'time':time,
                                 'nombre':nombre,'apellido':apellido,'pais':pais,'estado':estado,'codigo':codigo,
                                 'metodo':metodo,'numeroTarjeta':numeroTarjeta,'nombreTarjeta':nombreTarjeta,'expiracion':expiracion,'cvv':cvv})
        app_models_oracle.connection.commit()  
    else:
        return "404 BAD REQUEST", 400
    
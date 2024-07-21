from flask import Flask , flash, render_template  , request ,jsonify , redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from fileinput import filename 
import cx_Oracle 
import os
from datetime import date , datetime 
from werkzeug.utils import secure_filename
import requests
import json
import notificacionPush 

#hex_key_sec = "3d94d4e88fd24a7f8da5aa719b663a43"
#app.config["SECRET_KEY"] = hex_key_sec
#TBAR = DebugToolbarExtension(app)
#UPLOAD_FOLDER = r"C:\Users"

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/uploads"
ALLOWED_EXTENSIONS = set(['pdf','xlsx','txt','csv'])

try:
    connection=cx_Oracle.connect(
        user='user_boss',
        password='2024',
        dsn='localhost:1521/ORCL',
        encoding='UTF-8'

    )
except Exception as ex:
        print(ex)

def allowed_file(file):
    file = file.split('.')
    print(file)
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False
    
    #if request.method == 'POST':
     #   archivo = request.files['archivo']

      #  if archivo and allowed_file(archivo.filename):
       #     filename = secure_filename(archivo.filename)
        #    archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #else:
    

@app.route('/')

@app.route('/login.html')
def signup():
    return render_template('/login.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("Error404.html"), 404


@app.route("/toolbar", methods=["GET"])
def DEB_EX():
    return render_template("toolbar_key.html")

@app.route('/index.html')
def home():
    return render_template('/index.html')

@app.route('/portalPago.html')
def portal():
    return render_template('/portalPago.html')


@app.route('/dashboard.html')
def dashboard():
    return render_template('/dashboard.html')

@app.route('/modulo_cotizador.html')
def modulo_cotizador():
    return render_template('/modulo_cotizador.html')

@app.route('/crud_cotizador.html')
def crud_cotizador():
    return render_template('/crud_cotizador.html')


cursor = connection.cursor()



@app.route('/modulo_cotizador.html', methods=["POST"])
def carga():
    
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

        connection.commit() 

    return render_template('/index.html'),200
    
@app.route('/portalPago.html', methods=['POST'])
def pago():

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
        connection.commit()  
    else:
        return "404 BAD REQUEST", 400
    
    return render_template('/index.html'),200


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
    


@app.route('/formulario', methods=['POST'])
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
        INSERT INTO formulario_administrativo (nombre,apellido,tipo_evento,contacto,direccion,email,fecha,hora) 
        VALUES (:nombre,:apellido,:tipo_evento,:contacto,:direccion,:email,:fecha,:time)
        """

        cursor.execute(execute, {'nombre':nombre,'apellido':apellido,'tipo_evento':tipo_evento,'contacto':contacto,'direccion':direccion,'email':email,'fecha':fecha,'time':time})

        connection.commit()


    else:
        return "404  ERROR REQUEST", 400
     
    return render_template('/index.html') , 200


#cursor.execute("INSERT INTO DATOS_FACTURA VALUES ('jaime','jaimeretamal@gmail.com','joaquin palacios 556','990383265','15/07/24','18:04','JAIME','RETAMAL')")
for row in cursor.execute("select * from datos_factura"):
    print(row)
#connection.commit()


if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port=5000)
    
   

    

    



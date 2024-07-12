from flask import Flask, render_template  , request ,jsonify , redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
import cx_Oracle 
from datetime import date , datetime 
from werkzeug.utils import secure_filename
import requests
import json
import notificacionPush 


app = Flask(__name__)


hex_key_sec = "3d94d4e88fd24a7f8da5aa719b663a43"
app.config["SECRET_KEY"] = hex_key_sec
TBAR = DebugToolbarExtension(app)


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
def portalPago():
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


    
#cur = connection.cursor()
#cur.execute("SELECT * FROM SIGNUP WHERE HORA IS NOT NULL")
#for id_signup , email, clave_nueva , clave,fecha,nombre,apellido,hora in cur:
#    print("Campo: ", id_signup)
#    print("Campo: ", email)
#    print("Campo: ", clave_nueva)
#    print("Campo: ", clave)
#    print("Campo: ", fecha)
#    print("Campo: ", nombre)
#    print("Campo: ", apellido)
#    print("Campo: ", hora)


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


#hacer una insercion de portal pago 
@app.route('/portalPago', methods=['POST'])
def pag_registro_pago():
     #VARIABLES
    fecha = date.today()
    fechaHora = datetime.now()
    time = fechaHora.strftime("%H:%M:%S")

    if request.method == 'POST':
         
          nombre_completo = request.form['nombre']
          apellido_completo = request.form['apellido']
          nombre_usuario = request.form['usuario']
          email = request.form['email']
          direccion = request.form['direccion']
          telefono = request.form['telefono']
          pais = request.form['pais']
          estado = request.form['estado']
          codigo_postal = request.form['zip']
          tipo_tarjeta = request.form['check']
          nombre_tarjeta = request.form['nombreTarjeta']
          numero_cuenta = request.form['numeroTarjeta']
          expiracion = request.form['expiracion']
          cvv = request.form['cvv']
         
          execute = """
            INSERT INTO FACTURA_REGISTRO (nombre_completo,apellido_completo,nombre_usuario,email,direccion,telefono,pais,estado,codigo_postal,tipo_tarjeta,nombre_tarjeta ,numero_cuenta,expiracion,cvv,fecha,hora) 
             VALUES (:nombre_completo,:apellido_completo,:nombre_usuario,:email,:direccion,:telefono,:pais,:estado,:codigo_postal,:tipo_tarjeta,:nombre_tarjeta ,:numero_cuenta,:expiracion,:cvv,:fecha,:time)
          """
          
          cursor.execute(execute, {'nombre_completo':nombre_completo,'apellido_completo':apellido_completo,'nombre_usuario':nombre_usuario,'email':email,'direccion':direccion,'telefono':telefono,'pais':pais,'estado':estado,'codigo_postal':codigo_postal,'tipo_tarjeta':tipo_tarjeta,'nombre_tarjeta':nombre_tarjeta,'numero_cuenta':numero_cuenta,'expiracion':expiracion,'cvv':cvv,'fecha':fecha,'time':time})
          connection.commit()  

    else: 
        return "404 ERROR REQUEST", 400
    
    return render_template('/login.html'), 200



if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port=5000)
    
   

    

    



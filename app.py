from flask import Flask , flash, render_template  , request ,jsonify , redirect, url_for
#from flask_debugtoolbar import DebugToolbarExtension
from fileinput import filename 
import cx_Oracle 
import os
from datetime import date , datetime 
from werkzeug.utils import secure_filename
import requests
import json
#import app_notifPush 
from flask import make_response 
import app_models_oracle 
from app_controllers import *
import app_security_plsql



#hex_key_sec = "3d94d4e88fd24a7f8da5aa719b663a43"
#app.config["SECRET_KEY"] = hex_key_sec
#TBAR = DebugToolbarExtension(app)
#UPLOAD_FOLDER = r"C:\Users"

app = Flask(__name__)

@classmethod
def get_by_id(cls, id):

    return cls.query.filter(cls.id == id).first()

@app.route('/presupuesto.html')
def presupuesto():
    return render_template('/presupuesto.html')


@app.route('/login.html')
def signup():
    
    response = make_response("cookie_app")
    response.set_cookie("cookie_app","cookie")
    cookie_value = request.cookies.get("cookie_app")

    return render_template('/login.html')


@app.route('/modulo_formulario_administrativo.html')
def formulario_administrativo():

   cursor.execute("select * from formulario_administrativo")
   row = cursor.fetchall()

   return render_template('/modulo_formulario_administrativo.html', row = row)


@app.route('/editUser.html')
def edit_formulario():
   
   #x = cursor.execute("select * from formulario_administrativo")
   cursor.execute("select * from formulario_administrativo")
   row = cursor.fetchall()

   if row:
       
       nombre = request.form['nombre']
       apellido = request.form['apellido']
       tipo_evento = request.form['tipo_evento']
       contacto = request.form['contacto']
       direccion = request.form['direccion']
       email = request.form['email']
       fecha = request.form['fecha']
       hora = request.form['hora']

       row = row
   #row = ["jaime","retamal"]
   #data = edit_function(user)
   return render_template('/editUser.html', row=row)



@app.errorhandler(404)
def page_not_found(error):
    return render_template("Error404.html"), 404


@app.route("/toolbar", methods=["GET"])
def DEB_EX():
    return render_template("toolbar_key.html")


@app.route('/portalPago.html')
def portal():
    return render_template('/portalPago.html')

@app.route('/index.html')
def home():
    return render_template('/index.html')


@app.route('/dashboard.html')
def dashboard():
    return render_template('/dashboard.html')

@app.route('/modulo_cotizador.html')
def modulo_cotizador():
    return render_template('/modulo_cotizador.html')


@app.route('/adminDashboard.html')
def adminDash():

    return render_template('/adminDashboard.html')


cursor = app_models_oracle.connection.cursor()


@app.route('/index.html', methods=["POST"])
def login():
    return render_template('/index.html', miLogin = login_registro()), 200
    #MiProcedure = procedure_login()

@app.route('/login.html', methods=['POST'])
def signup_reg():
        
    return render_template('/login.html', miSignup = signup_registro()), 200
    #MiProcedure2 = procedure_signup 


@app.route('/modulo_cotizador.html', methods=["POST"])
def carga():
    
    return render_template('/index.html', miArchivo = registro_archivo()),200



@app.route('/crud_cotizador.html')
def cotizador():   
    for row in cursor.execute("select * from CRUD_ARCHIVO_COTIZACION"):
        
       
        return render_template('/crud_cotizador.html', campos=row), 200


    
@app.route('/portalPago.html', methods=['POST'])
def pago():

    return render_template('/index.html', miPago = registro_pago()),200




@app.route('/formulario', methods=['POST'])
def pag_formulario_administrativo():
    
    return render_template('/index.html', miFormulario = formulario_registro()) , 200
    #Miformulario = procedure_formulario()
    

if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost", port=5000)
    
   

    

    



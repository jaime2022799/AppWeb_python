from flask import Flask,flash, render_template , request , redirect, url_for
import requests 
from datetime import date , datetime 


app = Flask(__name__)

@app.route('/')



@app.route('/login.html', methods=['POST'])
def validacion_app():


    error_app = None

    while request.method == 'POST':
        
        if request.form['nombre'] != 'admin_manager' or \
                request.form['clave'] != 'admin_project_manager':
            error_app = "hay un error inesperado ..."
        else:
            flash("You were succesfully loggend in")

            return redirect(url_for('index.html'))
        
        if request.form['nombre'] != '':
            error_app = "Hay un error en el campo nombre verifique"
        else:
            flash("apellido ingresado correctamente")

        if request.form['apellido'] != '':

            error_app = "Hay un error en el campo apellido verifique"
        else:
            flash("apellido ingresado correctamente")
        

        if request.form['email'] != 'gmail.com':
            error_app = "Hay un error en el email ingresado verifique que sea gmail"
        else:
            flash("correo ingresado correctamente")

        

    return render_template('login.html', error_app=error_app)




@app.route('/index', methods=['POST'])
def pag_formulario_administrativo():

    error_app_2 = None
    

    while request.method == 'POST':

        if request.form['nombre'] != '' or  None:
            error_app_2 = "error en el campo nombre"
        else:
            flash("nombre ingresado correctamente")

        if request.form['apellido'] != '' or None:
            error_app_2 = "error en el campo apellido"
        else:
            flash("apellido ingresado correctamente")

        if request.form['tipo_evento'] != 'SISTEMA AUTOMOTRIZ' or 'SISTEMA HIPOTECARIO' or None:
            error_app_2 = "error en el campo tipo evento debe ser SISTEMA AUTOMOTRIZ o 'SISTEMA HIPOTECARIO"
        else:
            flash("tipo_evento ingresado correctamente")
        
        if request.form['contacto'] > 0  <= 9 or None:
            error_app_2 = "error en el campo contacto ingresar el 9 antes del numero"
        else:
            flash("apellido ingresado correctamente")

        if request.form['direccion'] != '' or None:
            error_app_2 = "error en el campo direccion Ingresar una direccion valida"
        else:
            flash("direccion ingresado correctamente")

        if request.form['email'] != 'gmail.com' or 'hotmail.con' or 'outlook.com' or None:
            error_app_2 = "error en el campo email"
        else:
            flash("email ingresado correctamente")

    
    return render_template('index.html', error_app_2=error_app_2)
     
   




    


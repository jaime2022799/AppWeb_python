from flask import flash,make_response ,  request , render_template
from datetime import date , datetime 
import cx_Oracle 
from werkzeug.utils import secure_filename
from fileinput import filename 
import os
import requests
import app
import app_models_oracle

#app.cotizador(campos)


def procedure_login():
        
    try:
        #llamar a la conexion del models oracle
        conexion = app_models_oracle.connection
        cur = conexion.cursor()

        #llamar a las variables 
        if request.method == 'POST':

            id_login = 1
            fecha = date.today()
            fechaHora = datetime.now()
            time = fechaHora.strftime("%H:%M:%S")
            email = request.form['email']
            clave = request.form['clave']

            cur.callproc("VALIDACION_SEGURIDAD_INSERT_LOGIN",(id_login,email,clave,fecha,time))
        else:
            print("Error en la ejecucion del procedimiento almacenado VALIDACION_SEGURIDAD_INSERT_LOGIN")

    except Exception as ex:
        print("A ocurrido un error en la conexion a la BD", ex)


    else:
        return "404 request", 400



def procedure_signup():
        
    try:
            #llamar a la conexion del models oracle
            conexion = app_models_oracle.connection
            cur = conexion.cursor()

            #llamar a las variables 
            if request.method == 'POST':


                fecha = date.today()
                fechaHora = datetime.now()
                time = fechaHora.strftime("%H:%M:%S")
                nombre = request.form['nombre']
                apellido = request.form['apellido']
                email = request.form['email']
                password_create = request.form['password_create']
                password_confirm = request.form['password_confirm']

                cur.callproc("VALIDACION_SEGURIDAD_INSERT_SIGNUP",(email,password_create,password_confirm,fecha,nombre,apellido,time))
            else:
                print("Error en la ejecucion del procedimiento almacenado VALIDACION_SEGURIDAD_INSERT_SIGNUP")

    except Exception as ex:
        print("A ocurrido un error en la conexion a la BD", ex)

    else:
        return "404 request", 400




def procedure_formulario():

    try:
            #llamar a la conexion del models oracle
            conexion = app_models_oracle.connection
            cur = conexion.cursor()

            #llamar a las variables 
            if request.method == 'POST':


                fecha = date.today()
                fechaHora = datetime.now()
                time = fechaHora.strftime("%H:%M:%S")
                nombre = request.form['nombre']
                apellido = request.form['apellido']
                tipo_evento = request.form['tipo_evento']
                contacto = request.form['contacto']
                direccion = request.form['direccion']
                email = request.form['email']

                cur.callproc("VALIDACION_INSERT_FORMULARIO_ADMINISTRATIVO",(nombre,apellido,tipo_evento,contacto,direccion,email,fecha,time))
            else:
                print("Error en la ejecucion del procedimiento almacenado VALIDACION_INSERT_FORMULARIO_ADMINISTRATIVO")

    except Exception as ex:
        print("A ocurrido un error en la conexion a la BD", ex)


    else:
        return "404 request", 400


def procedure_archivo():
    try:
            #llamar a la conexion del models oracle
            conexion = app_models_oracle.connection
            cur = conexion.cursor()

            #llamar a las variables 
            if request.method == 'POST':


                fecha = date.today()
                fechaHora = datetime.now()
                time = fechaHora.strftime("%H:%M:%S")
                nombre = 'Cotizacion_2024'

                file = request.files["archivo"]
                print(file)
                filename = secure_filename(file.filename)
                print(filename)
                if file and app.allowed_file(filename):
                    print('permitido')
                    file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))


                cur.callproc("VALIDACION_SEGURIDAD_INSERT_ARCHIVO",(nombre,fecha,time,filename))
            else:
                print("Error en la ejecucion del procedimiento almacenado VALIDACION_SEGURIDAD_INSERT_ARCHIVO")

    except Exception as ex:
        print("A ocurrido un error en la conexion a la BD", ex)


    else:
        return "404 request", 400



    # call VALIDACION_SEGURIDAD_INSERT_LOGIN()

    # call VALIDACION_SEGURIDAD_INSERT_SIGNUP()

    # call VALIDACION_INSERT_FORMULARIO_ADMINISTRATIVO()
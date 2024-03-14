import cx_Oracle 
from datetime import date
from flask import Flask , render_template ,  jsonify , request 


app = Flask(__name__)

@app.route('/')

@app.route('/login.html')
def pag_signup():
    return render_template('/login.html')

try:
    connection=cx_Oracle.connect(
        user='user_boss',
        password='2024',
        dsn='localhost:1521/ORCL',
        encoding='UTF-8'

    )
    print(connection.version)

    
    print('------------------------------------------------------------------------------------------')
        
    #def insertar_registro_signup():
    #  cursor=connection.cursor()
     # llamar_procedimiento= '''
     # call INSERTAR_REGISTRO_SIGNUP (15,'galeegalee2024@gmail.com','galeegalee2024','galeegalee2024','galeegalee','galeegalee')
     # '''
     # cursor.execute(llamar_procedimiento)
     # connection.commit()

    #insertar_registro_signup()
    def listar_signup():
      cursor=connection.cursor()
      cursor.execute("SELECT * FROM SIGNUP")
      rows=cursor.fetchall()
      for row in rows:
        print(row)
        
    listar_signup()

    print("----------------------------------------------------------------------------------------")

    #def insertar_registro_login():
    #  cursor=connection.cursor()
    #  llamar_sp_login = '''
    #  call INSERTAR_REGISTRO_LOGIN (8,'nicolasmendoza@gmail.com','mendoza',15)
    #  '''
    #  cursor.execute(llamar_sp_login)
    #  connection.commit()

    #insertar_registro_login()

    def listar_login():
      cursor=connection.cursor()
      cursor.execute("select * from login")
      filas=cursor.fetchall()
      for fila in filas:
        print(fila)

    listar_login()

    #def insertar_login():
     #  cursor=connection.cursor()

      # call_sp_login = '''
       # INSERT INTO LOGIN (ID_LOGIN,EMAIL,CLAVE,SIGNUP_ID,FECHA) VALUES (30,'jaimeretamal47@gmail.com','JAIME','29','21-01-2024')
       # '''
       #cursor.execute(call_sp_login)
       #connection.commit()
    #insertar_login()

    #print("--------------------------------------------------------------------------------------------")
        

except Exception as ex:
    print(ex)



fecha = date.today()

nombre_registro = 'JUAN'
apellido_registro = 'JARA'
email_registro = 'JASMANI@HOTMAIL.COM'
password__registro = 'JUAN'
password_registro_confirm = 'JUAN'




@app.route('/login.html', methods=["POST"])

def insertar_signup():
    
    cursor = connection.cursor()
    connection.autocommit = True
    #with connection.cursor() as cursor:

      #if request.method == "POST":

       # nombre = request.form['nombre']
        
        #apellido = request.form['apellido']
        #email = request.form['email']
        #password_create = request.form['password_create']
        #password_confirm = request.form['password_confirm']

    call_sp_signup = '''
        INSERT INTO SIGNUP (EMAIL,CLAVE_NUEVA,CLAVE,FECHA,NOMBRE,APELLIDO) VALUES (:email,:clave_nueva,:clave,:fecha,:nombre,:apellido)
        '''
    cursor.execute(call_sp_signup,[email_registro,password__registro,password_registro_confirm,fecha,nombre_registro,apellido_registro])
    connection.commit()

       # return render_template('/login.html')
      
      #else:
       # return "404 request"
        #return render_template('/index.html')
        #return redirect(url_for('/home'))
    #else:
    return "404 request"


#insertar_signup()




#x = 13
#y = 12
#p = 6

#def delete_registro_signup():
   
 #  cursor=connection.cursor()
 #  call_table_signup = f'''
 #  DELETE FROM SIGNUP WHERE ID_SIGNUP IN ('{x}','{y}','{p}')
  # '''
 #  cursor.execute(call_table_signup)
#   connection.commit()

  # return "404"

#delete_registro_signup()
    
    #else:
     #  return "404 Bad HTTPS"




   # llamar_procedimiento= '''
   # call INSERTAR_REGISTRO_SIGNUP (13,'pervis2024@gmail.com','pervis2024','pervis2024','pervis','mendoza')
   # '''
   # cursor.execute(llamar_procedimiento)
   # connection.commit()

   # connection.close()
   

#ejecutar_insertar_signup()
#cursor.execute("call INSERTAR_REGISTRO_SIGNUP(11,'gordon2024@gmail.com','gordon2024','gordon2024','gordon','gordon')")
#cursor.execute(insertar_usuario)
#connection.commit()

#connection.close()

import cx_Oracle 
from flask import Flask , render_template ,  jsonify

app = Flask(__name__)

try:
    connection=cx_Oracle.connect(
        user='user_boss',
        password='2024',
        dsn='localhost:1521/ORCL',
        encoding='UTF-8'

    )
    print(connection.version)

    def listar_signup():
      cursor=connection.cursor()
      cursor.execute("SELECT * FROM SIGNUP")
      rows=cursor.fetchall()
      for row in rows:
        print(row)
        
    listar_signup()

    print("----------------------------------------------------------------------------------------")

    #def insertar_registro_signup():
    #  cursor=connection.cursor()
     # llamar_procedimiento= '''
     # call INSERTAR_REGISTRO_SIGNUP (15,'galeegalee2024@gmail.com','galeegalee2024','galeegalee2024','galeegalee','galeegalee')
     # '''
     # cursor.execute(llamar_procedimiento)
     # connection.commit()

    #insertar_registro_signup()

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

    print("--------------------------------------------------------------------------------------------")
        
   

except Exception as ex:
    print(ex)


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


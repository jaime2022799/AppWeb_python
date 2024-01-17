import cx_Oracle , conexion_oracle 
from flask import Flask , render_template ,  jsonify , request , redirect, url_for

app = Flask(__name__)

@app.route('/login')
def pag_signup():
    return render_template('/login.html')


@app.route('/index.html')
def pag_index():
    return render_template('/index.html')


try:
    connection=cx_Oracle.connect(
        user='user_boss',
        password='2024',
        dsn='localhost:1521/ORCL',
        encoding='UTF-8'

    )
    


    @app.route('/login.html', methods=["POST"])
    def pag_signup_registro():
    
    #coneccion a oracle con cursor 
        cursor=connection.cursor()
        rows=cursor.fetchall()
        #variables name del html signup
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password_create = request.form['password_create']
        password_confirm = request.form['password_confirm']
    #llamamos al request del metodo post 
        if request.method == "POST":
            #  nombre = request.form['nombre']
            #  apellido = request.form['apellido']
            #  email = request.form['email']
            #  password_create = request.form['password_create']
            #  password_confirm = request.form['password_confirm']
             return render_template('/login.html')
        #return render_template('/index.html')
        #return redirect(url_for('/home'))
        else:
            return "404 request"
        
        
    
except Exception as ex:
    print(ex)





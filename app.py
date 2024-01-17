from flask import Flask, render_template , request , jsonify , redirect, url_for
import conexion_oracle 

app = Flask(__name__)


@app.route('/')

@app.route('/login.html')
def signup():
    return render_template('/login.html')


@app.route('/index.html')
def home():
    return render_template('/index.html')

#definimos la ruta de login para los parametros de la creacion de la cuenta signup
@app.route('/login.html', methods=["POST"])
def signup_registro():
    #llamamos al request del metodo post 
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password_create = request.form['password_create']
        password_confirm = request.form['password_confirm']
        return render_template('/login.html')
        #return render_template('/index.html')
        #return redirect(url_for('/home'))
    else:
        return "404 request"


#definimos la ruta de index para el registro de la cuenta creada pero en el login
@app.route('/index.html', methods=["POST"])
def login_registro():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
       
        return render_template('/index.html')
        #return render_template('/index.html')
        #return redirect(url_for('/home'))
    else:
        return "404 request"
    


if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port=5000)



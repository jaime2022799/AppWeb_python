
from flask import Flask ,render_template
from flask_debugtoolbar import DebugToolbarExtension
#importamos os y uuid
import os
import uuid

print(uuid.uuid4().hex)

print(os.urandom(24))

app = Flask(__name__)

app.debug = True
# app.config['SECRET_KEY']='Define_The_Key'



#asignar resultado de la clave a la variable key_secret
hex_key_sec = "3d94d4e88fd24a7f8da5aa719b663a43"
app.config["SECRET_KEY"] = hex_key_sec
TBAR = DebugToolbarExtension(app)


@app.route("/", methods=["GET"])
def DEB_EX():
    return render_template("toolbar_key.html")


if __name__ == "__main__":
    app.run()

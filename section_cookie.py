from flask import flask , Flask , make_response, request

app = Flask(__name__)

@app.route("/cookie_app")
def cookie_app():
    response = make_response("cookie_app")
    response.set_cookie("cookie_app","cookie")
    return response

@app.route("/cookie")
def cookie():
    cookie_value = request.cookies.get("cookie_app")
    return cookie_value

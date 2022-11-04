from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import back_end as be

app = Flask(__name__)
app.debug = True
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/add-post")
def add_post():
    return render_template("add-post.html")


@app.route("/posts", methods=["POST", "GET"])
def posts():
    if request.method == "POST":
        search_request = request.form['searchRequest']
        return search_request
    else:
        return "homo"


@app.route("/login", methods=["POST"])
def log_in():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        be.login(login, password)


@socketio.on('message')
def handle_message(message):
    print(message)
    if message != "User connected!":
        send(message, broadcast=True)


@app.route("/online-chat")
def online_chat():
    return render_template("online-chat.html")


if __name__ == "__main__":
    socketio.run(app, host="localhost", allow_unsafe_werkzeug=True)

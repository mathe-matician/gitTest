from flask import Flask, session

app = Flask(__name__)

@app.route("/")
def home() -> str:
    return "hello"

@app.route("/page1")
def page1() -> str:
    return "page 1"

@app.route("/page2")
def page2() -> str:
    return "page 2"

@app.route("/page3")
def page3() -> str:
    return "page 3"

@app.route("/login")
def do_login() -> str:
    session["logged_in"] = True
    return "You are now logged in"

@app.route("/logout")
def do_logout() -> str:
    session.pop("logged_in")
    return "You are now logged out"

@app.route("/status")
def check_status() -> str:
    if "logged_in" in session:
        return "You are currently logged in"
    return "You are NOT logged in"

app.secret_key = "YouWillNeverGuess"

if __name__ == "__main__":
    app.run(debug=True)

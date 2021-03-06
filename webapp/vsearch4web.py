from flask import Flask, render_template, request, escape, session, copy_current_request_context

from vsearch import search4letters

from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError

from checker import check_logged_in

from threading import Thread

from time import sleep


app = Flask(__name__)
app.config["dbconfig"] = {"host": "127.0.0.1",
                          "user": "vsearch",
                          "password": "pass",
                          "database": "vsearchlogDB"}

@app.route("/search4", methods=["POST"])
def do_search() -> "html":

    #current request context means it ensures that the HTTP request that
    #is active when a function is called remains active even when the
    #function is executed in a thread. A copy of the request context is
    #created and then pushed when the function is called.
    @copy_current_request_context 
    def log_request(req: "flask_request", res: str) -> None:
        sleep(15)#simulate long computing time
        try:
            with UseDatabase(app.config["dbconfig"]) as cursor:
                _SQL = """insert into log
                        (phrase, letters, ip, browser_string, results)
                        values
                        (%s, %s, %s, %s, %s)"""
                cursor.execute(_SQL, (req.form["phrase"],
                                      req.form["letters"],
                                      req.remote_addr,
                                      req.user_agent.browser,
                                      res ))
        except ConnectionError as err:
            print("Is your database connected? Error: ", str(err))
        except CredentialsError as err:
            print("User-ID/password issues. Error: ", str(err))
        except SQLError as err:
            print("Is your query correct? Error: ", str(err))
        return "Error"

    #flask.request is used below to access the keys in the
    #flask.request.form - aka the phrase and letters keys.
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "Here are your results:"
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target = log_request, args = (request, results))
        t.start()
    except Exception as err:
        print("***** There was an error connecting: ", str(err))
    return render_template("results.html",
                           the_phrase = phrase,
                           the_letters = letters,
                           the_title = title,
                           the_results = results)

@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    return render_template("entry.html",
                           the_title="Welcome to search4letters on the web!")

@app.route("/login")
def do_login():
    session["logged_in"] = True
    return "You are logged in now"

@app.route("/logout")
def do_logout():
    session.pop("logged_in")
    return "You have logged OUT"

@app.route("/viewlog")
@check_logged_in
def view_log() -> "html":

    try:
        with UseDatabase(app.config["dbconfig"]) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = ("Phrase", "Letters", "Remote_addr", "User_agent", "Results")
        return render_template("viewlog.html",
                               the_title = "App Request Log",
                               the_row_titles = titles,
                               the_data = contents)
    except ConnectionError as err:
        print("Is your database switched on? Error: ", str(err))
    except CredentialsError as err:
        print("User-ID/passsword issue. Error: ", str(err))
    except SQLError as err:
        print("Is your query correct? Error: ", str(err))
    except Exception as err:
        print("Something went wrong: ", str(err))

    return "Error"

app.secret_key = "YouWillNeverGuessMySecretKey"

if __name__ == "__main__":
    app.run(debug = True)

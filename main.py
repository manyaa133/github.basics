from flask import Flask

app=Flask(__name__)
@app.route("/")
def home():
    return "Hellow World!"
@app.route("/about")
def abc():
    return "This is the about route."

@app.route("/abc")
def abc():
    return "This is the ABC route."
@app.route("/<name>")
def greet(name):
    return f"Hello , {name}!"
if __name__ =="__main__":
    app.run(debug=True)
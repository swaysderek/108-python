from flask import Flask

app = Flask("Server")


@app.route("/")
def home():
    return "Hello from Flask"


@app.route("/me")
def about_me():
    return "Derek Urruita"




app.run(debug=True)
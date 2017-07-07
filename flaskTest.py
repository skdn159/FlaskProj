from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "HelloWorld"

if __name__ == "__flaskTest__":
    app.run(debug = True, host = '0,0,0,0', port = 5009)
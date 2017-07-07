from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "HelloWorld"

if __name__ == "__main__":
    app.run(debug = True, host = '127.0.0.1', port = 5009)


#while 1==True:
#    a = 10


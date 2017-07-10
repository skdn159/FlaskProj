from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for


app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "HelloWorld"

@app.route("/main")
def main():
    return "Here is mainPage"

@app.route("/login_form")
def login_form():
    return render_template("login_form.html")

@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        if(request.form['username'] =="ku"
            and request.form['password'] =="1234"):
            session["logged_in"] = True
            session["username"]= request.form['username']
            return request.form['username']+" 님 환영합니다"
        else:
            return "로그인 정보가 맞지 않습니다."
    else:
        return '잘못된 접근'

@app.route('/get_test', methods=['GET'])
def get_test():
    if request.method =='GET':
        if(request.args.get('username')=="ku"
           and request.args.get('password')=="1234"):
            return " Welcome " + request.args.get('username')+" !"
        else:
            return "로그인 정보가 맞지 않습니다."
    else:
        return '잘못된 접근'

@app.route('/logout')
def logout():
    session['logged_in']= False
    session.pop('username', None)
    return  redirect(url_for("main"))

secret_key = "sampleKey"

app.secret_key = "abc"




if __name__ == "__main__":
    app.run(debug = True, host = '127.0.0.1', port = 5009)




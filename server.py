from flask import Flask, Response, request, jsonify, json # importing the flask module and class Flask is mandatory
from user import Customer
import os
app = Flask(__name__, static_folder='docs')  # Flask constructor takes the


# Covert Dictionary to JSON
def dict_to_json(dct):
    return json.dumps(dct, sort_keys=True, indent=4, separators=(',', ': '))


customer = Customer()  # instantiating the class

data_sent = None


@app.before_request
def before():
    global data_sent
    if request.headers.get('Content-Type') == "application/json":
        data_sent = request.json
    else:
        print(request.headers.get('Content_Type'))
        print(request.data)
        data_sent = request.form


@app.route('/registration', methods= ['POST'])
def registration():
    try:
        if request.method == 'POST':
            firstName = data_sent.get('fname')
            surname = data_sent.get('surname')
            idNumber = data_sent.get('id')
            phoneNumber =data_sent.get('phone')
            email = data_sent.get('email')
            userName = data_sent.get('username')
            password = data_sent.get('password')
            print (firstName)
            result = customer.userRegistration(firstName, surname, idNumber,phoneNumber, email, userName, password)
            print("This is registration function result"+ str(result))
        else:
            result = {
                "success": False,
                "message": "use POST to feed data"
            }
    except Exception as error:
        result = {
            "success":False,
            "message":"An error occured " + str(error)
            }
    resp = Response(dict_to_json(result), mimetype="text/json")

    resp.headers["Access-Control-Allow-Origin"] = "profnaomi.github.io"  # Allow requester to access data
    return resp


@app.route('/login', methods= ['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print (email)
        result = customer.userLogin(email,password)
    else:
        result = {
            "success": False,
            "message": "use POST for this request"
        }
    
    return jsonify(result)


@app.route('/userProfileEdit', methods= ['POST'])
def userProfileEdit():
    if request.method == 'POST':
        userid = request.form.get('userid')
        sessiontoken = request.form.get('token')
        firstName = request.form.get('fname')
        surname = request.form.get('surname')
        username = request.form.get('username')
        print (firstName)
        result = customer.userProfileEdit(userid, sessiontoken, firstName, surname, username)
    else:
        result = {
            "success": False,
            "message": "use POST for this request"
        }
    
    return jsonify(result)


@app.route('/changePassword', methods= ['POST'])   
def changePassword():
    if request.method == 'POST':
        userid = request.form.get('userid')
        sessiontoken = request.form.get('token')
        oldPassword = request.form.get('oldPassword')
        newPassword = request.form.get('newPassword')
        print (newPassword, oldPassword)
        result = customer.changePassword(userid, sessiontoken, oldPassword,newPassword)
    else:
        result = {
            "success": False,
            "message": "use POST for this request"
        }

    return jsonify(result)


@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        userid = request.form.get('userid')
        sessiontoken = request.form.get('token')
        print(userid)
        result = customer.userLogout(userid,sessiontoken)
    else:
        result = {
            "success": False,
            "message": "use POST for this request"
        }
    
    return jsonify(result)


@app.route('/')
def hello_world():
    return app.send_static_file("index.html")


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

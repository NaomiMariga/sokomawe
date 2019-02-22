from flask import Flask, request, jsonify, json # importing the flask module and class Flask is mandatory
from user import Customer
app = Flask(__name__) # Flask constructor takes the 

customer = Customer() #instantiating the class


@app.route('/')
def hello_world():
    return "This an ecommerce API"

@app.route('/registration', methods= ['POST'])
def registration():
    try:
        if request.method == 'POST':
            firstName = request.form.get('fname')
            surname = request.form.get('surname')
            idNumber = request.form.get('id')
            phoneNumber =request.form.get('phone')
            email = request.form.get('email')
            userName = request.form.get('username')
            password = request.form.get('password')
            print (firstName)
            result = customer.userRegistration(firstName, surname, idNumber,phoneNumber, email, userName, password)
            
        else:
            result = {
                "success": False,
                "message": "use POST to feed data"
            }
    except Exception as error:
        result = "An error occured " + str(error)
    
    return jsonify(result)

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

@app.route('/logout', methods= ['POST'])
def logout():
    if request.method == 'POST':
        userid = request.form.get('userid')
        sessiontoken = request.form.get('token')
        print (userid)
        result = customer.userLogout(userid,sessiontoken)
    else:
        result = {
            "success": False,
            "message": "use POST for this request"
        }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run()


import sqlalchemy
from sqlalchemy import create_engine, String
from sqlalchemy.sql import text

class Customer:     
    engine = create_engine('postgres://vdjvyibgfeyiio:2d3c12435e93fe44ec5b7546dc7e494d5a0f7bac28b60bb325333ca1cd3a4e2c@ec2-23-21-165-188.compute-1.amazonaws.com:5432/ds3fhh163hsb1')
    sessions = []
    def ifEmailExists(self, email):
        sql = text("SELECT * FROM users")
        conn = self.engine.connect()
        result = conn.execute(sql)
        rows= result.fetchall()
        print ("this is my test 1"+ str(result))
        print ("this is my test 2"+ str(rows))
        try:
            for row in rows:
                dbemail = row['email']
                All_emails = []
                All_emails.append(dbemail)
                print ("this is my test 3 " + str(All_emails))
            if email in All_emails: 
                return True
            else:
                return False
        except Exception as error:
            "An error occured " + str(error)

    def userRegistration(self,firstName, surname, idNumber,phoneNumber, email, userName, password):
        if firstName.strip() is not "":
            if surname.strip() is not "":
                if idNumber.strip() is not "":
                    if phoneNumber.strip is not "":
                        if email.strip() is not "":
                            if not self.ifEmailExists(email):
                                if userName.strip() is not "":
                                    if password.strip() is not "": 
                                        try:
                                            conn = self.engine.connect()
                                            sql= text("INSERT INTO users (firstName, surname, idNumber, phoneNumber, email, userName, password) VALUES (:firstName, :surname, :idNumber, :phoneNumber, :email, :userName, :password)")
                                            sql = sql.bindparams(firstName=firstName, surname=surname, idNumber=idNumber, phoneNumber=phoneNumber, email=email, userName=userName, password=password)
                                            conn.execute(sql)
                                            conn.close()
                                            message = {"success": True,
                                            "message": "user created successfully",
                                            "user": { "firstName": firstName, "email": email}
                                            }
                                        except Exception as error:
                                            message = "an error occured " + str(error)
                                    else:
                                        message= "password cannot be blank"
                                else:
                                    message= "provide username"
                            else:
                                message = "user already exists"
                        else:
                            message= "provide a valid email"
                    else:
                        message= "phone number cannot be blank"
                else:
                    message= " please provide ID number"
            else:
                message= "surname cannot be blank"
        else:
            message= "please provide your given name"
        
        return {"message":message}
    
    def userLogin(self, email, password):
        if email:
            if password:
                print( "this is test 1" + email)
                try:
                    conn = self.engine.connect()
                    sql = text("SELECT userid, email, username, password FROM users WHERE email = :email")
                    sql = sql.bindparams(email=email)
                    print ("This is test 2" + email)
                    result = conn.execute(sql)
                    row = result.fetchone()
                    print ("This is test 3" + str(row))
                    dbemail = row['email']
                    dbpassword = row['password']
                    dbuser = row['username']
                    dbuserid = row['userid']   
                    print ("This is test 3" + dbuser)
                    if email == dbemail and password == dbpassword:    
                        message = {
                            "success":True,
                            "message":"Welcome "+ dbuser + ", Your login was sucessful",
                        "userid":dbuserid,
                        "token":"1234testtoken"}
                        sql = text("INSERT INTO sessions (userid, sessiontoken) VALUES (:userid, :token)")
                        sql = sql.bindparams(userid=dbuserid, token=message["token"])
                        conn.execute (sql)
                    else:
                        message = "Email and Password did not match"
                except Exception as error:
                    message = "An error occured " + str(error)
                
            else:
                message = " Please provide password"
        else:
            message = "please provide email"

        return {"message": message}

    def userIsLoggedIn(self, userid, sessiontoken):
        conn = self.engine
        sql = text("SELECT * FROM sessions WHERE userid=%i" % userid)
        result = conn.execute(sql)
        rows = result.fetchall()
        dbsessionid = None
        message = "User not found"
        print("This is a test 1 " + str(rows))
        for row in rows:
            print("This is a test 2 " + str(row))
            dbsessionid= row['sessionid']
            dbsessionuserid= row['userid']
            dbsessiontoken= row['sessiontoken']
            print("This is a test 3 "+ dbsessiontoken, dbsessionuserid)
            print("This is a test 3 "+ sessiontoken, userid)
            
        try:
            if int(userid) == dbsessionuserid and sessiontoken == dbsessiontoken:
                message = {
                    "sessionId": dbsessionid,
                    "userid": dbsessionuserid,
                    "token": dbsessiontoken}
                print("This is a test 4 %s" % str(message))
                return True, message
            else:
                return False, message
        except Exception as error:
            message = "An error occured " + str(error)
        return message

    def userLogout(self, userid, sessiontoken):
        if self.userIsLoggedIn(userid, sessiontoken):
            try:
                sessionid= self.sessions[0]
                print ("This is test 12 " + str(sessionid))
                conn = self.engine
                sql = text("DELETE FROM sessions WHERE sessionid=:sessionid")
                sql= sql.bindparams(sessionid=sessionid)
                conn.execute(sql)
                message = "Sucessfully logged out"
            except Exception as error:
                message = "An error occured " + str(error)
        else:
            message = "You must be logged in to log out"
        return {"message":message}
            
    def userProfileEdit(self, userid,sessiontoken, firstName, surname, username):
        if self.userIsLoggedIn(userid, sessiontoken):
            if firstName:
                sql = text("UPDATE users SET firstname=:firstName WHERE userid=:userid")
                sql = sql.bindparams(firstName=firstName, userid=userid)
                print("testy 1")
                conn = self.engine
                conn.execute(sql)
                message = "Firstname updated successfully"
            elif surname:
                sql = text("UPDATE users SET surname=:surname WHERE userid=:userid")
                sql = sql.bindparams(surname=surname,userid=userid)
                conn = self.engine
                conn.execute(sql)
                print("testy 2")
                message = "surname updated successfully"
            elif username:
                sql = text("UPDATE users SET username=:username WHERE userid=:userid")
                try:
                    sql = sql.bindparams(username=username,  userid=userid)
                    conn = self.engine
                    conn.execute(sql)
                    message = " username Updated successfully"
                except Exception as error:
                    message = "An error occured " + str(error)
            else:
                sql = text("UPDATE users SET username=:username WHERE userid=:userid")

                message = "Provide either firsname, surname or username"
        else:
            message= "Please log in to continue"
        return {"message":message}

    def changePassword(self,userid,sessiontoken,oldPassword,newPassword):
        if self.userIsLoggedIn(userid,sessiontoken):
            if oldPassword:
                if newPassword.strip() is not "":
                    try:
                        sql = text("SELECT * FROM users WHERE userid=:userid")
                        conn = self.engine
                        sql = sql.bindparams(userid=userid)
                        result = conn.execute(sql)
                        row = result.fetchone()
                        dbpassword = row['password']
                        if oldPassword == dbpassword:
                            sql = text("UPDATE users SET password=:password WHERE userid=:userid")
                            sql = sql.bindparams(password=newPassword, userid=userid)
                            conn = self.engine
                            conn.execute(sql)
                            message = "password updated"
                        else:
                            message = "Passwords did not match"
                    except Exception as error:
                        message = "An error occured " + str(error)
                else:
                    message = "password cannot be blank"
            else:
                message = "Provide your current password"        
        else:
            message = "You seemto be logged out, login to change password"
        return {"message":message}


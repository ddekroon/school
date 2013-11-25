import logging
import MySQLdb

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from myapp.lib.base import BaseController, render

log = logging.getLogger(__name__)


def dbConnect():
    db = MySQLdb.connect(host="localhost",
                user="root", # replace with your username
                passwd="skittles", # replace with your password (student id number, including leading 0)
                db="cis3210") # course database
    
    #db = MySQLdb.connect(host="dursley.socs.uoguelph.ca",
    #            user="ddekroon", # replace with your username
    #            passwd="0709999", # replace with your password (student id number, including leading 0)
    #            db="cis3210") # course database
    return db

def getUsers(db):
    db.query("""SELECT userid, username FROM users""")
    result = db.store_result()
    tuples = result.fetch_row(0)
    db.close()

    users = []
    for row in tuples:
        users.append(row)
    return users



class MaincontrollerController(BaseController):


    def users(self, userid):
        db = dbConnect()

        if request.cookies.get('userid'):
            return render('login.mako')
        
        c.addError = 0
        c.userAdded = 0
        if 'newUsername' in request.params:
            newUsername = request.params['newUsername']
            c.newUserSet = 1
            newPassword = request.params['newPassword']
            dbCursor = db.cursor()
            if newUsername == '':
                c.addError = 1
            if newPassword == '':
                c.addError = 1
            if newUsername != '' and newPassword != '':
                db.query("""SELECT count(*) as numRows, MAX(userid) as maxUserID FROM users""")
                result = db.store_result()
                data = result.fetch_row(1, 1)
                if data[0]['numRows'] == 0:
                    newUserID = 1
                else:
                    newUserID = data[0]['maxUserID'] + 1
                newUsername = MySQLdb.escape_string(newUsername)
                newPassword = MySQLdb.escape_string(newPassword)
                c.newUsername = newUsername
                c.newPassword = newPassword
                dbCursor.execute("""INSERT INTO users (userid, username, password) VALUES (%s, %s, %s)""", (newUserID, newUsername, newPassword))
                db.commit()
                c.userAdded = 1

        if 'delUser' in request.params:
            toDelete = request.params['delUser']
            dbCursor = db.cursor()
            dbCursor.execute("""DELETE FROM users WHERE userid = %s""", (toDelete,))
            db.commit()
            c.userDeleted = 1
        else:
            c.userDeleted = 0


        if 'delAllUsers' in request.params:
            dbCursor = db.cursor()
            dbCursor.execute("""DELETE FROM users""")
            db.commit()
            c.userDeleted = 2
        
        c.user = getUsers(db)
        

        c.loginError = 0
        return render('/users.mako')

    def login(self):

        if request.cookies.get('userid'):
            return render('login.mako')        
        else:
            db = dbConnect()
            dbCursor = db.cursor()
            if 'username' in request.params:
                username = request.params['username']
                password = request.params['password']
            else:
                username = ''
                password = ''
            
            dbCursor.execute("""SELECT count(*) as numRows FROM users where username=%s AND password=%s""", (username, password))
            data = dbCursor.fetchone()

            if data[0] != 0:
                response.set_cookie('userid', username, max_age=180*24*3600 )
                return render('login.mako')
            else:
                c.loginError = 1
                c.deleteAll = 0
                c.toDelete = 0
                c.newUserSet = 0
                c.userAdded = 0
                c.userDeleted = 0
                c.addError = ''
                c.user = getUsers(db)
                return render('users.mako')
    
    def logout(self):
        if response.delete_cookie('userid'):
            c.logoutSuccess = 0
        else:
            c.logoutSuccess = 1
        return render('logout.mako')    

    def main(self):
        if 'inputText' in request.params:
            c.inputText = request.params['inputText']
            if c.inputText == '':
                c.noImages = 1
                c.error = 'Please enter a string to search'
                c.perPage = 0
            else:
                c.inputText = request.params['inputText']
                c.perPage = request.params['numPictures']
                c.noImages = 0
        else:
            c.inputText = ''
            c.perPage = 0
            c.noImages = 1
            c.error = 'Please enter information to search flickr images'
        return render('main.mako')

    def lab1(self):
        return render('lab1.mako')

    def index(self):
        # Return a rendered template
        #return render('/application.mako')
        # or, return a string
        return render('index.mako')


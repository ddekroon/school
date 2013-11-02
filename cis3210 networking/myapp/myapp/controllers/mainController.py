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

class MaincontrollerController(BaseController):


    def users(self, userid):
        if request.cookies.get('userid'):
            return render('login.mako')
     
        if 'newUsername' in request.params:
            c.newUsername = request.params['newUsername']
            c.newUserSet = 1
            c.newPassword = request.params['newPassword']
        else:
            c.newUsername = ''
            c.newUserSet = 0
            c.newPassword = ''

        if 'delUser' in request.params:
            c.toDelete = request.params['delUser']
        else:
            c.toDelete = 0 

        if 'delAllUsers' in request.params:
            c.deleteAll = 1
        else:
            c.deleteAll = 0
        
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
                return render('users.mako')
    
    def logout(self):
        if response.delete_cookie('userid'):
            c.logoutSuccess = 0
        else:
            c.logoutSuccess = 1
        return render('logout.mako')    

    def main(self):
	return render('main.mako')

    def lab1(self):
        return render('lab1.mako')

    def index(self):
        # Return a rendered template
        #return render('/application.mako')
        # or, return a string
        return render('index.mako')


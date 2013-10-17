import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from myapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MaincontrollerController(BaseController):

    def users(self, userid):
        if 'AddUser' in request.params:
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

        return render('/users.mako')

    def lab1(self):
        return render('/lab1.mako')

    def index(self):
        # Return a rendered template
        #return render('/application.mako')
        # or, return a string
        return render('/index.mako')

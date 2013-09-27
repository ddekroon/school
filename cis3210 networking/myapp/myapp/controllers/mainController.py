import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from myapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MaincontrollerController(BaseController):

    def lab2(self, userid):
        if 'userid' in request.params:
            c.userid = request.params['userid']
        else:
            c.userid = userid
        
        if 'useridPost' in request.params:
            c.useridPost = request.params['useridPost']
        else:
            c.useridPost = 'N/A'

        return render('/lab2.mako')

    def lab1(self):
        # Return a rendered template
        #return render('/application.mako')
        # or, return a string
        return render('/lab1.mako')

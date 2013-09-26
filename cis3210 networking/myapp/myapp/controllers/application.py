import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from myapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ApplicationController(BaseController):

    def lab2(self, userid, age):
        c.userid = userid
        c.age = age
        return render('/lab2.mako')

    def lab1(self):
        # Return a rendered template
        #return render('/application.mako')
        # or, return a string
        return render('/base.mako')

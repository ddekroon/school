import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from myapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MaincontrollerController(BaseController):

    def lab2(self, userid):
        c.attributes = request.params.getall('attributes')
        if 'userid' in request.params:
            userids = request.params.getall('userid')
        else:
            userids = [userid]

        if 'updateData' in request.params:
            del userids[-1]


        if 'delName' in request.params:
            toDelete = request.params['delName']
            del userids[int(toDelete)]
            del userids[-1]
            del c.attributes[int(toDelete)]

        c.userids = userids
        count = 0
        for user in c.userids:
            if count >= len(c.attributes):
                c.attributes.append('')

            count += 1
        return render('/lab2.mako')

    def lab1(self):
        # Return a rendered template
        #return render('/application.mako')
        # or, return a string
        return render('/lab1.mako')

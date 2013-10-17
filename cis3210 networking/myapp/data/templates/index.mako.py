# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
<<<<<<< HEAD
_magic_number = 8
_modified_time = 1382031059.474845
_enable_loop = True
_template_filename = '/media/derek/Files/workspace/school/cis3210 networking/myapp/myapp/templates/index.mako'
_template_uri = '/index.mako'
_source_encoding = 'utf-8'
=======
_magic_number = 6
_modified_time = 1381357453.270224
_template_filename='/media/Files/workspace/school/cis3210 networking/myapp/myapp/templates/index.mako'
_template_uri='/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
>>>>>>> 4987be0623aa45556bc88d0a278b3ce223b9f50a
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
<<<<<<< HEAD
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n\t<title>Derek Dekroon 0709999</title>\n\t<script src="/js/jquery.js"></script>\n\t<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>\n\t<link href=\'/css/bootstrap.min.css\' rel=\'stylesheet\' />\n\t<link href=\'/css/myStyle.css\' rel=\'stylesheet\' />\n  </head>\n  <body>\n    <div class=\'mainSection\'>\n        <h1>Home Page</h1>\n        <h3>Links</h3>\n\t<ul>\n\t    <li><a href=\'/lab1\'>Lab 1</a></li>\n\t    <li><a href=\'/users\'>Users Page</a></li>\n\t</ul>\n        <div class=\'description\'>\n\t\t<h4>Lab 5</h4>\n\t\t<p>To use this lab, go to the <a href=\'/users\'>Users Page</a>. From there you can add a new user using the form at the bottom, delete a user using the delete individual users button, or delete all users. When you add a new user the username and password get escaped using the MySQLdb.escape_string() function. You must have something written in for both username AND password (strlen > 0) in order for the insert to work.\n\t\t</p>\n        </div>\n    </div>\n  </body>\n</html>\n')
=======
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n\t<title>Derek Dekroon 0709999</title>\n\t<script src="/js/jquery.js"></script>\n\t<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>\n\t<link href=\'/css/bootstrap.min.css\' rel=\'stylesheet\' />\n\t<link href=\'/css/myStyle.css\' rel=\'stylesheet\' />\n  </head>\n  <body>\n    <div class=\'mainSection\'>\n        <h1>Home Page</h1>\n        <h3>Links</h3>\n\t<ul>\n\t    <li><a href=\'/lab1\'>Lab 1</a></li>\n\t    <li><a href=\'/users\'>Users Page</a></li>\n\t</ul>\n\t<p>Select any of the links to go to the pages required for the lab you wish to do.</p>\n    </div>\n  </body>\n</html>\n')
>>>>>>> 4987be0623aa45556bc88d0a278b3ce223b9f50a
        return ''
    finally:
        context.caller_stack._pop_frame()



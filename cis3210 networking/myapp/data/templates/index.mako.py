# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1382560694.249351
_enable_loop = True
_template_filename = '/media/derek/Files/workspace/school/cis3210 networking/myapp/myapp/templates/index.mako'
_template_uri = '/index.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n\t<title>Derek Dekroon 0709999</title>\n\t<script src="/js/jquery.js"></script>\n\t<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>\n\t<link href=\'/css/bootstrap.min.css\' rel=\'stylesheet\' />\n\t<link href=\'/css/myStyle.css\' rel=\'stylesheet\' />\n  </head>\n  <body>\n    <div class=\'mainSection\'>\n        <h1>Home Page</h1>\n        <h3>Links</h3>\n\t<ul>\n\t    <li><a href=\'/lab1\'>Lab 1</a></li>\n\t    <li><a href=\'/users\'>Users Page</a></li>\n\t</ul>\n        <div class=\'description\'>\n\t\t<h4>Lab 6</h4>\n\t\t<div class=\'list\'><ol><li>To use this lab, go to the <a href=\'/users\'>Users Page</a>.</li>\n<li>You\'ll probably need to create a user using the register option on the top navigation bar.</li> \n<li>After you create a user you can log in using the log in form in the top navigation bar.</li>\n<li>When you log in a cookie will be created on the browser then you\'ll be redirected to the login page.</li>\n<li>You can go to /users, or /login and since you already have that cookie you\'ll automatically be directed to the successful login page.</li>\n<li>To delete the cookie, select the logout option in the navigation bar of the login page.</li>\n<li>The log out destroys the cookie, and from the log out page you can either log in or go to the users page.</li>\n\t\t</ol></div>\n        </div>\n\t<p>Select any of the links to go to the pages required for the lab you wish to do.</p>\n    </div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



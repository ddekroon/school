# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1381269305.757605
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n\t<title>Derek Dekroon App</title>\n\t<script src="/js/jquery.js"></script>\n\t<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>\n\t<link href=\'/css/bootstrap.min.css\' rel=\'stylesheet\' />\n\t<link href=\'/css/myStyle.css\' rel=\'stylesheet\' />\n  </head>\n  <body>\n    <div class=\'mainSection\'>\n        <h1>Home Page</h1>\n        <h3>Links</h3>\n\t<ul>\n\t    <li><a href=\'/lab1\'>Lab 1</a></li>\n\t    <li><a href=\'/users\'>Users Page</a></li>\n\t</ul>\n    </div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


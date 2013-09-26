# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1380153595.781777
_enable_loop = True
_template_filename = '/media/derek/Files/School/CIS 3210 Networking/myapp/myapp/templates/lab2.mako'
_template_uri = '/lab2.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<title>Test #3</title>\n</head>\n<body>\n<h1>Test #3</h1>\n<p>Hello user ')
        # SOURCE LINE 7
        c.userid 
        
        __M_writer(u'.</p>\n<p>Age ')
        # SOURCE LINE 8
        c.age 
        
        __M_writer(u'.</p>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



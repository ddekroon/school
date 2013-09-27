# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1380245212.461996
_enable_loop = True
_template_filename = '/media/derek/Files/workspace/school/cis3210 networking/myapp/myapp/templates/lab2.mako'
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
        __M_writer(u'<html>\n<head>\n<title>Lab 2</title>\n</head>\n<body>\n<form name="lab2form" action="" method="PUT">\n<h1>')
        # SOURCE LINE 7
        __M_writer(escape( c.userid))
        __M_writer(u'</h1>\n<p>Userid:\n<input type="text" name="userid" value= ')
        # SOURCE LINE 9
        __M_writer(escape(c.userid))
        __M_writer(u' />\n</p>\n<p>\n<input type="submit" name="submit" value="submit using PUT" />\n</p>\n</form>\n<form name="lab2form" action="" method="POST">\n<h1>')
        # SOURCE LINE 16
        __M_writer(escape( c.useridPost))
        __M_writer(u'</h1>\n<p>Userid:\n<input type="text" name="useridPost" value= ')
        # SOURCE LINE 18
        __M_writer(escape(c.useridPost))
        __M_writer(u' />\n</p>\n<p>\n<input type="submit" name="submit" value="submit using POST" />\n</p>\n</form>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



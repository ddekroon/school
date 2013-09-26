# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1380062053.405425
_enable_loop = True
_template_filename = '/media/derek/Files/School/CIS 3210 Networking/myapp/myapp/templates/base.mako'
_template_uri = '/base.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n\t<title>Derek Dekroon A1</title>\n\t<script src="/js/jquery.js"></script>\n  <script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>\n\t\n\t<link href=\'/css/bootstrap.min.css\' rel=\'stylesheet\' />\n\t\n\t<style>\n\t\t#myDiv {\n\t\t\theight:100px;\n\t\t\twidth:100px;\n\t\t\tbackground-color:blue;\n\t\t}\n\t</style>\n  </head>\n  <body>\n    <button class=\'btn-success\' id=\'myButton\'>Toggle Data</button>\n\t<div id=\'myDiv\'>Div to hide</div>\n\n\t<script type=\'text/javascript\'>\n\t\t$(\'#myButton\').click(function(){\n\t\t\t$(\'#myDiv\').toggle("fold", 1000 );\n\t\t});\n\t</script>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



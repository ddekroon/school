# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1385352933.307168
_template_filename='/media/Files/workspace/school/cis3210 networking/myapp/myapp/templates/index.mako'
_template_uri='index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n\t<title>Derek Dekroon 0709999</title>\n\t<script src="/js/jquery.js"></script>\n\t<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>\n\t<link href=\'/css/bootstrap.min.css\' rel=\'stylesheet\' />\n\t<link href=\'/css/myStyle.css\' rel=\'stylesheet\' />\n  </head>\n  <body>\n    <div class=\'mainSection\'>\n        <h1>Home Page</h1>\n        <h3>Links</h3>\n\t<ul>\n\t    <li><a href=\'/lab1\'>Lab 1</a></li>\n\t    <li><a href=\'/users\'>Users Page</a></li>\n\t    <li><a href=\'/main\'>Flickr Page</a></li>\n        </ul>\n        <div class=\'description\'>\n\t\t<h4>Lab 7</h4>\n\t\t<div class=\'list\'><p>To use this lab, go to the <a href=\'/main\'>Flickr Page</a>.\nThis time you\'ll be taken to a page with no data by default. Click the Flickr link in the tool bar at the top of the page. Fill in the pop up however you want and press check flick or hit enter. Your images should show up. If you don\'t put any input the program will catch it. By default only 1 image will show up.\n            </p></div>\n        </div>\n\t<p>Select any of the links to go to the pages required for the lab you wish to do.</p>\n    </div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



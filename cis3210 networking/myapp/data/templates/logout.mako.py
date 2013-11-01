# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1382558910.768039
_enable_loop = True
_template_filename = '/media/derek/Files/workspace/school/cis3210 networking/myapp/myapp/templates/logout.mako'
_template_uri = '/logout.mako'
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
        __M_writer(u'\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>Derek Dekroon 0709999</title>\n\n    <!-- Bootstrap core CSS -->\n    <link href="/css/bootstrap.css" rel="stylesheet">\n    <!-- Bootstrap theme -->\n    <link href="/css/bootstrap-theme.min.css" rel="stylesheet">\n\n    <!-- Custom styles for this template -->\n    <link href="/css/theme.css" rel="stylesheet">\n    <link href="/css/style.css" rel="stylesheet">\n    <link href="/css/myStyle.css" rel="stylesheet">\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n      <script src="/js/html5shiv.js"></script>\n      <script src="/js/respond.min.js"></script>\n    <![endif]-->\n    <link rel="stylesheet" href="/css/jquery-ui.css" />\n    <script src="http://code.jquery.com/jquery-1.9.1.js"></script>\n    <script src="/js/bootstrap.min.js"></script>\n    <script src="/js/holder.js"></script>\n    <script src="js/jquery-ui.js"></script>\n    <script>\n      $(document).ready(function() {\n        $( "#log-in" ).dialog({\n        autoOpen: false,\n        height: 300,\n        width: 350,\n        modal: true,\n        buttons: {\n          "Log In": function() {\n            $("#loginForm").submit();\n          },\n          "Cancel": function() {\n            $( this ).dialog( "close" );\n          },\n        }\n        });\n\n        $( "#login" ).button().click(function() {\n          $( "#log-in" ).dialog( "open" );\n        });\n      });\n    </script>\n  </head>\n\n  <body> \n\n    <div id="log-in" title="Log in">\n      <p class="validateTips">All form fields are required.</p>\n      <form id=\'loginForm\' action=\'/login\' method=\'post\'>\n        <table>\n\t  <tr>\n\t    <td>User Name</td><td><input type="text" name="username" id="name" class="text ui-widget-content ui-corner-all" /></td>\n          </tr><tr>\n            <td>Password</td><td><input type="password" name="password" id="password" value="" class="text ui-widget-content ui-corner-all" /></td>\n          </tr>\n         </table>\n      </form>\n    </div>\n\n    <!-- Fixed navbar -->\n    <div class="navbar navbar-inverse navbar-fixed-top">\n      <div class="container">\n        <div class="navbar-header">\n          <a class="navbar-brand" href="#">Logged Out</a>\n        </div>\n        <div class="navbar-collapse collapse">\n          <ul class="nav navbar-nav">\n            <li><a href="/users">Home</a></li>\n            <li><a href="#" id=\'login\'>Log In</a></li>\n          </ul>\n        </div><!--/.nav-collapse -->\n      </div>\n    </div>\n\n\n    <div class="container theme-showcase">\n      \n')
        # SOURCE LINE 89
        if c.logoutSuccess == 1:
            # SOURCE LINE 90
            __M_writer(u"    <p class='panel panel-success'>Successfully logged out</p>\n")
            # SOURCE LINE 91
        else:
            # SOURCE LINE 92
            __M_writer(u"    <p class='panel panel-danger'>Error logging out, credentials don't exist</p>\n")
        # SOURCE LINE 94
        __M_writer(u'    </div> <!-- /container -->\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



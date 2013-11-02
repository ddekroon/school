# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383345442.052195
_template_filename='/media/Files/workspace/school/cis3210 networking/myapp/myapp/templates/users.mako'
_template_uri='/users.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        endfor = context.get('endfor', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        import json
        import MySQLdb
        
        #db = MySQLdb.connect(host="dursley.socs.uoguelph.ca",
        #                    user="ddekroon", # replace with your username
        #                    passwd="0709999", # replace with your password (student id number, including leading 0)
        #                    db="cis3210") # course database
        
        db = MySQLdb.connect(host="localhost",
                            user="root", # replace with your username
                            passwd="skittles", # replace with your password (student id number, including leading 0)
                            db="cis3210") # course database
        
        
        userDeleted = 0
        if c.deleteAll == 1:
            dbCursor = db.cursor()
            dbCursor.execute("""DELETE FROM users""")
            db.commit()
            userDeleted = 2
        
        if c.toDelete != 0:
            dbCursor = db.cursor()
            dbCursor.execute("""DELETE FROM users WHERE userid = %s""", (c.toDelete,))
            db.commit()
            userDeleted = 1
        
        
        userAdded = 0
        addError = 0
        if c.newUserSet == 1:
            dbCursor = db.cursor()
            if c.newUsername == '':
                addError = 1
            if c.newPassword == '':
                addError = 1
            if c.newUsername != '' and c.newPassword != '':
                db.query("""SELECT count(*) as numRows, MAX(userid) as maxUserID FROM users""")
                result = db.store_result()
                data = result.fetch_row(1, 1)
                if data[0]['numRows'] == 0:
                    newUserID = 1
                else:
                    newUserID = data[0]['maxUserID'] + 1
                newUsername = MySQLdb.escape_string(c.newUsername)
                newPassword = MySQLdb.escape_string(c.newPassword)
                dbCursor.execute("""INSERT INTO users (userid, username, password) VALUES (%s, %s, %s)""", (newUserID, newUsername, newPassword))
                db.commit()
                userAdded = 1
            
        db.query("""SELECT * FROM users""")
        r = db.store_result()
        tuples = r.fetch_row(0)
        db.close()
        
        usernames = []
        for user in tuples:
            usernames.append(user)
        endfor
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dbCursor','addError','usernames','newUserID','user','newPassword','db','userDeleted','tuples','json','MySQLdb','userAdded','result','r','data','newUsername'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 61
        __M_writer(u'\n\n\n\n\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>Derek Dekroon 0709999</title>\n\n    <!-- Bootstrap core CSS -->\n    <link href="/css/bootstrap.css" rel="stylesheet">\n    <!-- Bootstrap theme -->\n    <link href="/css/bootstrap-theme.min.css" rel="stylesheet">\n\n    <!-- Custom styles for this template -->\n    <link href="/css/theme.css" rel="stylesheet">\n    <link href="/css/style.css" rel="stylesheet">\n    <link href="/css/myStyle.css" rel="stylesheet">\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n      <script src="/js/html5shiv.js"></script>\n      <script src="/js/respond.min.js"></script>\n    <![endif]-->\n    <link rel="stylesheet" href="/css/jquery-ui.css" />\n    <script src="http://code.jquery.com/jquery-1.9.1.js"></script>\n    <script src="/js/bootstrap.min.js"></script>\n    <script src="/js/holder.js"></script>\n    <script src="js/jquery-ui.js"></script>\n    <script>\n      $(document).ready(function() {\n        $( "#log-in" ).dialog({\n        autoOpen: false,\n        height: 300,\n        width: 350,\n        modal: true,\n        buttons: {\n          "Log In": function() {\n            $("#loginForm").submit();\n          },\n          "Cancel": function() {\n            $( this ).dialog( "close" );\n          },\n        }\n        });\n\n        $( "#login" ).button().click(function() {\n          $( "#log-in" ).dialog( "open" );\n        });\n\n        $( "#create-user" ).dialog({\n        autoOpen: false,\n        height: 300,\n        width: 350,\n        modal: true,\n        buttons: {\n          "Create Account": function() {\n            $("#newUserForm").submit();\n          },\n          "Cancel": function() {\n            $( this ).dialog( "close" );\n          },\n        }\n        });\n \n        $( "#register" ).button().click(function() {\n          $( "#create-user" ).dialog( "open" );\n        });\n      });\n    </script>\n  </head>\n\n  <body> \n\n    <div id="create-user" title="Create new user">\n      <p class="validateTips">All form fields are required.</p>\n      <form id=\'newUserForm\' method=\'post\'>\n        <table>\n\t  <tr>\n\t    <td>User Name</td><td><input type="text" name="newUsername" id="name" class="text ui-widget-content ui-corner-all" /></td>\n          </tr><tr>\n            <td>Password</td><td><input type="password" name="newPassword" id="password" value="" class="text ui-widget-content ui-corner-all" /></td>\n          </tr>\n         </table>\n      </form>\n    </div>\n\n    <div id="log-in" title="Log in">\n      <p class="validateTips">All form fields are required.</p>\n      <form id=\'loginForm\' action=\'/login\' method=\'post\'>\n        <table>\n\t  <tr>\n\t    <td>User Name</td><td><input type="text" name="username" id="name" class="text ui-widget-content ui-corner-all" /></td>\n          </tr><tr>\n            <td>Password</td><td><input type="password" name="password" id="password" value="" class="text ui-widget-content ui-corner-all" /></td>\n          </tr>\n         </table>\n      </form>\n    </div>\n\n    <!-- Fixed navbar -->\n    <div class="navbar navbar-inverse navbar-fixed-top">\n      <div class="container">\n        <div class="navbar-header">\n          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n          </button>\n          <a class="navbar-brand" href="#">Users Page</a>\n        </div>\n        <div class="navbar-collapse collapse">\n          <ul class="nav navbar-nav">\n            <li><a href="#">Home</a></li>\n            <li><a href="#" id=\'register\'>Register</a></li>\n            <li><a href="#" id=\'login\'>Log In</a></li>\n            <!-- <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>\n              <ul class="dropdown-menu">\n                <li><a href="#">Action</a></li>\n                <li><a href="#">Another action</a></li>\n                <li><a href="#">Something else here</a></li>\n                <li class="divider"></li>\n                <li class="dropdown-header">Nav header</li>\n                <li><a href="#">Separated link</a></li>\n                <li><a href="#">One more separated link</a></li>\n              </ul>\n            </li> -->\n          </ul>\n        </div><!--/.nav-collapse -->\n      </div>\n    </div>\n\n\n    <div class="container theme-showcase">\n      \n')
        # SOURCE LINE 203
        if userAdded == 1:
            # SOURCE LINE 204
            __M_writer(u"    <p class='panel panel-success'>User ")
            __M_writer(escape(c.newUsername))
            __M_writer(u' added</p>\n')
            pass
        # SOURCE LINE 206
        if userDeleted == 1:
            # SOURCE LINE 207
            __M_writer(u"    <p class='panel panel-success'>User deleted</p>\n")
            pass
        # SOURCE LINE 209
        if userDeleted == 2:
            # SOURCE LINE 210
            __M_writer(u"    <p class='panel panel-success'>All users deleted</p>\n")
            pass
        # SOURCE LINE 212
        if addError == 1:
            # SOURCE LINE 213
            __M_writer(u"    <p class='panel panel-warning'>Error adding user, information not filled out correctly</p>\n")
            pass
        # SOURCE LINE 215
        if c.loginError == 1:
            # SOURCE LINE 216
            __M_writer(u"    <p class='panel panel-warning'>Error logging in, credentials don't exist</p>\n")
            pass
        # SOURCE LINE 218
        __M_writer(u'<form name="usersForm" id=\'userForm\' action="" method="POST">\n')
        # SOURCE LINE 219
        counter = 0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u"\n<table class='userTable' id='table1'>\n    <tr>\n        <th>ID</th><th class='second-column'>UserName</th><th class='third-column'>Del</th>\n    </tr>\n")
        # SOURCE LINE 224
        for user in usernames:
            # SOURCE LINE 225
            __M_writer(u"    <tr>\n    <td class='first-column'>")
            # SOURCE LINE 226
            __M_writer(escape(user[0]))
            __M_writer(u"</td><td class='second-column'>")
            __M_writer(escape(user[1]))
            __M_writer(u"</td><td class='third-column'>\n        <button name='delUser' value='")
            # SOURCE LINE 227
            __M_writer(escape(user[0]))
            __M_writer(u"'>Delete User</button>\n    </td></tr>\n    ")
            # SOURCE LINE 229
 
            counter = counter + 1 
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 231
            __M_writer(u'\n')
            pass
        # SOURCE LINE 233
        __M_writer(u'    <tr>\n\t<td colspan=2></td><td>\n            <button name=\'delAllUsers\' value=\'1\'>Delete All</button>\n        </td>\n    </tr>\n    </table>\n\n    \n\n\n<!-- <div class=\'addUser\'>\n    <h1>New User</h1>\n    <p>Username:\n    <input type="text" name="newUsername"  />\n    </p>\n    <p>Password: \n    <input type="text" name="newPassword" />\n    </p><p>\n        <input type="submit" name="AddUser" value="Add User" />\n        </p>\n    </div> -->\n</form>\n    </div> <!-- /container -->\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



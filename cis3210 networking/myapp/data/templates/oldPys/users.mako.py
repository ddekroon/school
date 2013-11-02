# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382397329.793241
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
        #"""
#Using http://mysql-python.sourceforge.net/MySQLdb.html
#
#An example to get you started on CIS*3210 Lab 5.
#"""
        
        import MySQLdb
        
        db = MySQLdb.connect(host="dursley.socs.uoguelph.ca",
                            user="ddekroon", # replace with your username
                            passwd="0709999", # replace with your password (student id number, including leading 0)
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
        if c.newUserSet == 1:
            dbCursor = db.cursor()
            if c.newUsername == '':
                print "ERROR, Username = Null"
            if c.newPassword == '':
                print "ERROR, new password = Null"
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
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dbCursor','usernames','newUserID','user','newPassword','db','userDeleted','tuples','json','MySQLdb','userAdded','result','r','data','newUsername'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 60
        __M_writer(u"\n<html>\n<head>\n<title>Derek Dekroon 0709999</title>\n<script src='/js/jquery.js'></script>\n<link type='text/css' rel='stylesheet' href='/css/style.css'>\n\n</head>\n<body>\n")
        # SOURCE LINE 69
        if userAdded == 1:
            # SOURCE LINE 70
            __M_writer(u"    <p class='success'>User ")
            __M_writer(escape(c.newUsername))
            __M_writer(u' added</p>\n')
            pass
        # SOURCE LINE 72
        if userDeleted == 1:
            # SOURCE LINE 73
            __M_writer(u"    <p class='success'>User deleted</p>\n")
            pass
        # SOURCE LINE 75
        if userDeleted == 2:
            # SOURCE LINE 76
            __M_writer(u"    <p class='success'>All users deleted</p>\n")
            pass
        # SOURCE LINE 78
        __M_writer(u'<form name="lab2form" action="" method="POST">\n')
        # SOURCE LINE 79
        counter = 0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u"\n<table class='userTable' id='table1'>\n    <tr>\n        <th>ID</th><th>UserName</th><th>Password</th><th>Del</th>\n    </tr>\n")
        # SOURCE LINE 84
        for user in usernames:
            # SOURCE LINE 85
            __M_writer(u"    <tr>\n    <td>\n    <input type='text' name='id' value='")
            # SOURCE LINE 87
            __M_writer(escape(user[0]))
            __M_writer(u"' />\n    <td>\n    <input type='text' name='username' value='")
            # SOURCE LINE 89
            __M_writer(escape(user[1]))
            __M_writer(u"' />\n    </td><td>\n    <input type='text' name='id' value='")
            # SOURCE LINE 91
            __M_writer(escape(user[2]))
            __M_writer(u"' />\n    </td><td>\n    <button name='delUser' value='")
            # SOURCE LINE 93
            __M_writer(escape(user[0]))
            __M_writer(u"'>Delete User</button>\n    </td></tr>\n    ")
            # SOURCE LINE 95
 
            counter = counter + 1 
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 97
            __M_writer(u'\n')
            pass
        # SOURCE LINE 99
        __M_writer(u'    <tr>\n\t<td colspan=3></td><td>\n            <button name=\'delAllUsers\' value=\'1\'>Delete All</button>\n        </td>\n    </tr>\n    </table>\n    <div class=\'addUser\'>\n    <h1>New User</h1>\n    <p>Username:\n    <input type="text" name="newUsername"  />\n    </p>\n    <p>Password: \n    <input type="text" name="newPassword" />\n    </p><p>\n        <input type="submit" name="AddUser" value="Add User" />\n        </p>\n    </div>\n</form>\n</body>\n </html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



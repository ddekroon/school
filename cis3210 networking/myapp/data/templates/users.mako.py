# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1381359360.678401
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
        
        usernames = []
        for user in c.userids:
            usernames.append(user)
        endfor
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['json','usernames','user'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 8
        __M_writer(u'\n<html>\n<head>\n<title>Derek Dekroon 0709999</title>\n<script src=\'/js/jquery.js\'></script>\n<link type=\'text/css\' rel=\'stylesheet\' href=\'/css/style.css\'>\n\n</head>\n<body>\n<form name="lab2form" action="" method="POST">\n')
        # SOURCE LINE 18
        counter = 0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u"\n<table class='userTable'>\n    <tr>\n        <th>UserID</th><th>Attribute</th><th>Del</th>\n    </tr>\n")
        # SOURCE LINE 23
        for user in usernames:
            # SOURCE LINE 24
            __M_writer(u"    <tr>\n    <td>\n    <input type='text' name='userid' value='")
            # SOURCE LINE 26
            __M_writer(escape(user))
            __M_writer(u"' />\n    </td><td>\n        <input type='text' name='attributes' value='")
            # SOURCE LINE 28
            __M_writer(escape(c.attributes[counter]))
            __M_writer(u"' />\n    </td><td>\n    <button name='delName' value='")
            # SOURCE LINE 30
            __M_writer(escape(counter))
            __M_writer(u"'>Delete User</button>\n    </td></tr>\n    ")
            # SOURCE LINE 32
 
            counter = counter + 1 
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 34
            __M_writer(u'\n')
            pass
        # SOURCE LINE 36
        __M_writer(u'    <tr>\n\t<td colspan=2>\n            <input type=\'submit\' name=\'updateData\' class=\'centreButton\' value=\'Update Data\' />\n        </td><td>\n            <button name=\'deleteAll\' value=\'1\'>Delete All</button>\n        </td>\n    </tr>\n    </table>\n    <h1>New User</h1>\n    <p>Userid:\n    <input type="text" name="userid"  />\n    </p>\n    <p>\n    <input type="submit" name="submit" value="Add User" />\n    </p>\n</form>\n</body>\n </html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



<%
import json
"""
Using http://mysql-python.sourceforge.net/MySQLdb.html

An example to get you started on CIS*3210 Lab 5.
"""

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
%>
<html>
<head>
<title>Derek Dekroon 0709999</title>
<script src='/js/jquery.js'></script>
<link type='text/css' rel='stylesheet' href='/css/style.css'>

</head>
<body>
% if userAdded == 1:
    <p class='success'>User ${c.newUsername} added</p>
%endif
%if userDeleted == 1:
    <p class='success'>User deleted</p>
%endif
%if userDeleted == 2:
    <p class='success'>All users deleted</p>
%endif
<form name="lab2form" action="" method="POST">
<% counter = 0 %>
<table class='userTable'>
    <tr>
        <th>ID</th><th>UserName</th><th>Password</th><th>Del</th>
    </tr>
% for user in usernames:
    <tr>
    <td>
    <input type='text' name='id' value='${user[0]}' />
    <td>
    <input type='text' name='username' value='${user[1]}' />
    </td><td>
    <input type='text' name='id' value='${user[2]}' />
    </td><td>
    <button name='delUser' value='${user[0]}'>Delete User</button>
    </td></tr>
    <% 
    counter = counter + 1 
    %>
% endfor
    <tr>
	<td colspan=3></td><td>
            <button name='delAllUsers' value='1'>Delete All</button>
        </td>
    </tr>
    </table>
    <div class='addUser'>
    <h1>New User</h1>
    <p>Username:
    <input type="text" name="newUsername"  />
    </p>
    <p>Password: 
    <input type="text" name="newPassword" />
    </p><p>
        <input type="submit" name="AddUser" value="Add User" />
        </p>
    </div>
</form>
</body>
 </html>

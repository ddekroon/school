<%
import json

usernames = []
for user in c.userids:
    usernames.append(user)
endfor
%>
<html>
<head>
<title>Lab 2</title>
<script src='/js/jquery.js'></script>
<link type='text/css' rel='stylesheet' href='/css/style.css'>

</head>
<body>
<form name="lab2form" action="" method="POST">
<% counter = 0 %>
<table class='userTable'>
    <tr>
        <th>UserID</th><th>Attribute</th><th>Del</th>
    </tr>
% for user in usernames:
    <tr>
    <td>
    <input type='text' name='userid' value='${user}' />
    </td><td>
        <input type='text' name='attributes' value='${c.attributes[counter]}' />
    </td><td>
    <button name='delName' value='${counter}'>Delete User</button>
    </td></tr>
    <% 
    counter = counter + 1 
    %>
% endfor
    <tr>
	<td colspan=2>
            <input type='submit' name='updateData' class='centreButton' value='Update Data' />
        </td><td>
            <button name='deleteAll' value='1'>Delete All</button>
        </td>
    </tr>
    </table>
    <h1>New User</h1>
    <p>Userid:
    <input type="text" name="userid"  />
    </p>
    <p>
    <input type="submit" name="submit" value="Add User" />
    </p>
</form>
</body>
 </html>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Derek Dekroon 0709999</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.css" rel="stylesheet">
    <!-- Bootstrap theme -->
    <link href="/css/bootstrap-theme.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/css/theme.css" rel="stylesheet">
    <link href="/css/style.css" rel="stylesheet">
    <link href="/css/myStyle.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="/js/html5shiv.js"></script>
      <script src="/js/respond.min.js"></script>
    <![endif]-->
    <link rel="stylesheet" href="/css/jquery-ui.css" />
    <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/holder.js"></script>
    <script src="js/jquery-ui.js"></script>
    <script>
      $(document).ready(function() {
        $( "#log-in" ).dialog({
        autoOpen: false,
        height: 300,
        width: 350,
        modal: true,
        buttons: {
          "Log In": function() {
            $("#loginForm").submit();
          },
          "Cancel": function() {
            $( this ).dialog( "close" );
          },
        }
        });

        $( "#login" ).button().click(function() {
          $( "#log-in" ).dialog( "open" );
        });

        $( "#create-user" ).dialog({
        autoOpen: false,
        height: 300,
        width: 350,
        modal: true,
        buttons: {
          "Create Account": function() {
            $("#newUserForm").submit();
          },
          "Cancel": function() {
            $( this ).dialog( "close" );
          },
        }
        });
 
        $( "#register" ).button().click(function() {
          $( "#create-user" ).dialog( "open" );
        });
      });
    </script>
  </head>

  <body> 

    <div id="create-user" title="Create new user">
      <p class="validateTips">All form fields are required.</p>
      <form id='newUserForm' method='post'>
        <table>
	  <tr>
	    <td>User Name</td><td><input type="text" name="newUsername" id="name" class="text ui-widget-content ui-corner-all" /></td>
          </tr><tr>
            <td>Password</td><td><input type="password" name="newPassword" id="password" value="" class="text ui-widget-content ui-corner-all" /></td>
          </tr>
         </table>
      </form>
    </div>

    <div id="log-in" title="Log in">
      <p class="validateTips">All form fields are required.</p>
      <form id='loginForm' action='/login' method='post'>
        <table>
	  <tr>
	    <td>User Name</td><td><input type="text" name="username" id="name" class="text ui-widget-content ui-corner-all" /></td>
          </tr><tr>
            <td>Password</td><td><input type="password" name="password" id="password" value="" class="text ui-widget-content ui-corner-all" /></td>
          </tr>
         </table>
      </form>
    </div>

    <!-- Fixed navbar -->
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Users Page</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="/">Menu</a></li>
            <li><a href="#" id='register'>Register</a></li>
            <li><a href="#" id='login'>Log In</a></li>
            <!-- <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li> -->
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>


    <div class="container theme-showcase">
      
% if c.userAdded == 1:
    <p class='panel panel-success'>User ${c.newUsername} added</p>
%endif
%if c.userDeleted == 1:
    <p class='panel panel-success'>User deleted</p>
%endif
%if c.userDeleted == 2:
    <p class='panel panel-success'>All users deleted</p>
%endif
%if c.addError == 1:
    <p class='panel panel-warning'>Error adding user, information not filled out correctly</p>
%endif
%if c.loginError == 1:
    <p class='panel panel-warning'>Error logging in, credentials don't exist</p>
%endif
<form name="usersForm" id='userForm' action="" method="POST">
<% counter = 0 %>
<table class='userTable' id='table1'>
    <tr>
        <th>ID</th><th class='second-column'>UserName</th><th class='third-column'>Del</th>
    </tr>
% for userObj in c.user:
    <tr>
    <td class='first-column'>${userObj[0]}</td><td class='second-column'>${userObj[1]}</td><td class='third-column'>
        <button name='delUser' value='${userObj[0]}'>Delete User</button>
    </td></tr>
    <% 
    counter = counter + 1 
    %>
% endfor
    <tr>
	<td colspan=2></td><td>
            <button name='delAllUsers' value='1'>Delete All</button>
        </td>
    </tr>
    </table>

    


<!-- <div class='addUser'>
    <h1>New User</h1>
    <p>Username:
    <input type="text" name="newUsername"  />
    </p>
    <p>Password: 
    <input type="text" name="newPassword" />
    </p><p>
        <input type="submit" name="AddUser" value="Add User" />
        </p>
    </div> -->
</form>
    </div> <!-- /container -->
  </body>
</html>


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
      });
    </script>
  </head>

  <body> 

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
          <a class="navbar-brand" href="#">Logged Out</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="/users">Home</a></li>
            <li><a href="#" id='login'>Log In</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>


    <div class="container theme-showcase">
      
%if c.logoutSuccess == 1:
    <p class='panel panel-success'>Successfully logged out</p>
%else:
    <p class='panel panel-danger'>Error logging out, credentials don't exist</p>
%endif
    </div> <!-- /container -->
  </body>
</html>

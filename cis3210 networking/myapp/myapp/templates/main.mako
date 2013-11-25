<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
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
    <!-- Custom styles for this template -->
    <link href="/css/style.css" rel="stylesheet">
    <link href="/css/myStyle.css" rel="stylesheet">
    <link rel="stylesheet" href="/css/jquery-ui.css" />

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="../../assets/js/html5shiv.js"></script>
      <script src="../../assets/js/respond.min.js"></script>
    <![endif]-->
    <script src="/js/jquery.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/holder.js"></script> 
    <script src="js/jquery-ui.js"></script>
	<script>
		$(document).ready(function() {
			$( "#search-menu" ).dialog({
			autoOpen: false,
			height: 300,
			width: 350,
			modal: true,
			buttons: {
			  "Get Pictures": function() {
				$("#searchForm").submit();
			  },
			  "Cancel": function() {
				$( this ).dialog( "close" );
			  },
			}
			});

			$( "#searchMenu" ).button().click(function() {
			  $( "#search-menu" ).dialog( "open" );
			});
		});
    </script>
    
  </head>

  <body>
	  
	<div id="search-menu" title="Search Flickr">
      <p class="validateTips">All form fields are required.</p>
		<form method="post" action="/main" id="searchForm">
			<table>
				<tr>
					<td>
						Search String
					</td><td>
						<input class='inputField'  type='text' name='inputText' class="text ui-widget-content ui-corner-all" />
					</td>
				</tr><tr>
					<td>
						# of Pictures
					</td><td>
						<select class='inputField' name="numPictures" class="text ui-widget-content ui-corner-all">
							% for x in range(1, 11):
							<option value=${x}>${x}</option>
							%endfor
						</select>
					</td>
				</tr>
			</table>	
		</form>
    </div>

    <!-- Fixed navbar -->
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Main page</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="/">Menu</a></li>
            <li><a href="#" id='searchMenu'>Search Flickr</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container theme-showcase">
		%if c.noImages == 1:
			<h2>${c.error}</h2>
		%endif
		<div style='height:300px;' id='picContainer'></div>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    
    <script type='text/javascript'>
    function flickrHandler(rsp) {
      //window.rsp = rsp;
      var s = "";
      // http://farm{id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg
      // http://www.flickr.com/photos/{user-id}/{photo-id}
      s = "total number is: " + rsp.photos.photo.length + "<br/>";
    
      for (var i=0; i < rsp.photos.photo.length; i++) {
        photo = rsp.photos.photo[i];
        t_url = "http://farm" + photo.farm + ".static.flickr.com/" + 
          photo.server + "/" + photo.id + "_" + photo.secret + "_" + "t.jpg";
        p_url = "http://www.flickr.com/photos/" + photo.owner + "/" + photo.id;
        s +=  '<a href="' + p_url + '">' + '<img style="padding:3px;height:200px;width:200px;" alt="'+ photo.title + 
          '"src="' + t_url + '"/>' + '</a>';
      }
      //alert(s);
      $('#picContainer').html(s);
    }
    </script>
    <script src="http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=2bfe2a46e8884e2bcd7cb20be75b7db6&tags=${c.inputText}&per_page=${c.perPage}&format=json&jsoncallback=flickrHandler"></script> 
  </body>
</html>

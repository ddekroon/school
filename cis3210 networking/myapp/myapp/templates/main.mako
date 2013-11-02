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

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="../../assets/js/html5shiv.js"></script>
      <script src="../../assets/js/respond.min.js"></script>
    <![endif]-->

    
  </head>

  <body>

    <!-- Fixed navbar -->
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Log in page</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a id='logout' href="/logout">Log Out</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container theme-showcase">
	<div style='height:200px;' id='picContainer'></div>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/js/jquery.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/holder.js"></script> 
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
    <script src="http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=98321bf69d4fa7cce3f182ecf1c29376&tags=construction&per_page=5&format=json&jsoncallback=flickrHandler"></script> 
  </body>
</html>

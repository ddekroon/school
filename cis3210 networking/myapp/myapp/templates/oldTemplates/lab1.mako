<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
	<title>Derek Dekroon 0709999</title>
	<script src="/js/jquery.js"></script>
  <script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
	
	<link href='/css/bootstrap.min.css' rel='stylesheet' />
	
	<style>
		#myDiv {
			height:100px;
			width:100px;
			background-color:blue;
		}
	</style>
  </head>
  <body>
    <button class='btn-success' id='myButton'>Toggle Data</button>
	<div id='myDiv'>Div to hide</div>

	<script type='text/javascript'>
		$('#myButton').click(function(){
			$('#myDiv').toggle("fold", 1000 );
		});
	</script>
  </body>
</html>

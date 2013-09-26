<%inherit file="/base.mako" />

<%def name="head_tags()">
<srcipt src="/js/bootstrap.js" type='text/javascript'></script>
<srcipt src="/js/jquery.js" type='text/javascript'></script>
<link href='/css/bootstrap.min.css' rel='stylesheet' />
<link href='/css/bootstrap.responsive.css' rel='stylesheet' />
<script>
	$('document').ready(function(){
		$('#myButton').click(function(){
			alert('Hi!');
		});
	});
</script>
</%def>

<button id='myButton' value='HI!'>Click Me</button>

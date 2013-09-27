<html>
<head>
<title>Lab 2</title>
</head>
<body>
<form name="lab2form" action="" method="PUT">
<h1>${ c.userid}</h1>
<p>Userid:
<input type="text" name="userid" value= ${c.userid} />
</p>
<p>
<input type="submit" name="submit" value="submit using PUT" />
</p>
</form>
<form name="lab2form" action="" method="POST">
<h1>${ c.useridPost}</h1>
<p>Userid:
<input type="text" name="useridPost" value= ${c.useridPost} />
</p>
<p>
<input type="submit" name="submit" value="submit using POST" />
</p>
</form>
</body>
</html>

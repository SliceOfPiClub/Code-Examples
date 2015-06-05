<!DOCTYPE html>
<html>
<head>
</head>
<script>
function turnON()
{
	window.location.href = '/on';
}
function turnOFF()
{
	window.location.href = '/off';
}
</script>
<body>
	<form acion="/toggle" method="get">
	<p>Click the buttons to turn the device ON or OFF</p>
	<input type='button' onClick='turnON()' value=' TURN ON '/>
	<input type='button' onClick='turnOFF()' value=' TURN OFF '/>
	</form>
</body>
</html>

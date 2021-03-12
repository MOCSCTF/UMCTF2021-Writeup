<?php
error_reporting(0);
ini_set('open_basedir','.');
if(isset($_POST['viewsource'])){
	highlight_file(__FILE__);
	die();
}

mt_srand(mktime());

function de_code($value){
	$value = base64_decode($value);
	$result = '';
	for($i=0;$i<strlen($value);$i++){
		$result .= chr(ord($value[$i])-$i*2);
	}
	return $result;
}

if(!( file_get_contents($_GET['1234']) === 'MOCTF_is_good' && mt_rand(1,10000) === intval($_GET['go_Lakers']))){
	header('location:https://www.google.com');
}else{
	echo 'great';
}

echo file_get_contents(de_code($_GET['file_']));

?>




<!DOCTYPE html>
<html>
<head>
	<title>HAHAHA</title>
</head>
<body>
<h3>Where is the flag???</h3>
<h3>Capture the flag (CTF) is a traditional outdoor sport</h3><h3> where two or more teams each have a flag (or other markers) and the objective is to capture the other team's flag,</h3> <h3>located at the team's "base", and bring it safely back to their own base.</h3><h3> Enemy players can be "tagged" by players in their home territory and,</h3> depending on the rules, they may be out of the game, become members of the opposite team, sent back to their own territory,<h3></h3> or frozen in place ("in jail") until freed by a member of their own team.</h3>
</body>
</html>

























































































































<!-- post me viewsource -->















<!-- thanks me, go check flag.php -->

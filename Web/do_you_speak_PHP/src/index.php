<?php
include '/flag.php';
show_source(__FILE__);

// Stage 1
if (isset($_GET['text'])) {
	$text = $_GET['text'];
	if(@file_get_contents($text)!=="кеeр"){
        die("You must speak my language a different way!</br>");
	}
	echo "Stage 1 is complete! You unlocked the key: <b>".$secretkey."</b></br>";
}


// Stage 2
if (isset($_GET['key1'])) {
	$key1 = $_GET['key1'];
	$keyId = 1314;
	if (intval($key1) !== $keyId || $key1 === $keyId) {
    	die(""."what's your problem</br>");
	}
	echo "flag first part: <b>".$flag1."</b></br>";
	echo "Stage 2 is complete! Keep Going!</br>";
}


// Stage 3
if (isset($_GET['hash'])&&isset($_GET['token'])&&isset($_GET['keyId'])) {
	$hash = $_GET['hash'];
	$token = intval($_GET['token']);
	if(substr(hash("sha256", $keyId + $token . $secretkey), 5, 25) == $hash) {
    	$keyId = $_GET['keyId'];
	} else {
    	die("Out!</br>");
	}
	echo "flag second part: <b>".$flag2."</b></br>";
	echo "Stage 3 is complete! You defeated death, for now...</br>";
}


// stage 4
if (isset($_GET['key2'])&&isset($_GET['keyId'])) {
	$key2=$_GET['key2'];
	if ($keyId==$key2) {
		die("i don't expect they are same</br>");
	} elseif (sha1($keyId)===sha1($key2)) {
		echo "Final stage is complete Congratulations</br>";
	} else {
		die("They are even not equal..</br>");
	}
	echo "flag final part: <b>".$flag3."</b></br>";
	echo "<b>".$flag1.$flag2.$flag3."</b></br>"; 
}
?>

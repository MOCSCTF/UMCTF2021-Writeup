<?php

function en_code($value){

    $result = '';
    for($i=0;$i<strlen($value);$i++){
        $result .= chr(ord($value[$i])+$i*2);

    }
    $value = base64_encode($result);
    return $value;
}

echo en_code($_GET['code']);

?>

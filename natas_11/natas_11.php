#!/usr/bin/env php

<?php

    //this script will be ran by natas_11.py

    $decodedCookie = $argv[1];

    $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

    $plain = json_encode($defaultdata); 
    $cipher = base64_decode($decodedCookie);

    function xor_encrypt($in, $key) {

        $text = $in;
        $outText = '';

        // Iterate through each character and do xor
        for($i = 0; $i < strlen($text) ; $i++) {
        
            $outText .= $text[$i] ^ $key[$i % strlen($key)];

        }

        return $outText;

    }

    $out = substr(xor_encrypt($plain, $cipher), 0, 4);

    $newData = array("showpassword" => "yes", "bgcolor"=>"#ffffff");
    $newDataJSON = json_encode($newData);
    $secret = base64_encode(xor_encrypt($newDataJSON, $out));

    echo $secret 

?>
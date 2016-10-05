<?php
function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$c = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
print base64_encode(xor_encrypt($c)) . "\n";
?>

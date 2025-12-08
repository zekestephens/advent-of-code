#!/usr/bin/env php
<?php
$key = file_get_contents('input');
$i = 0;
$found5Zeros = False;
while (true) {
    $m = md5("$key$i");
    if (!$found5Zeros && str_starts_with($m, "00000")) {
        echo "$i\n";
        $found5Zeros = True;
    }
    if (str_starts_with($m, "000000")) {
        echo "$i\n";
        break;
    }
    $i++;
}

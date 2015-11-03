<?php
	$fileName = 'mobiles.json';
	$data = file_get_contents($fileName);
	$phpMobiles = json_decode($data);
	print_r($phpMobiles);
?>
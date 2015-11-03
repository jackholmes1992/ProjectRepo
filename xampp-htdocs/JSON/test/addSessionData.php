<?php
	/* An example of manipulating a JSON file */

	$session = array(
		'clipId' => '333333',
		'position' => '00.00.00.00',
		'creator' => 'Laura'
	);


	$file = 'session.json';
	echo "Raw contents of JSON...<br><br>";
	print_r(file_get_contents($file));

	echo "<br><br>JSON data decoded so data is usable in PHP...<br><br>";
	$json = json_decode(file_get_contents($file),true);
	print_r($json);

	echo "<br><br>Additional data added to JSON data via PHP...<br><br>";
	array_push($json['session'],$session);
	print_r($json);

	echo "<br><br>Data encoded back to JSON...<br><br>";
	$json = json_encode($json);
	print_r($json);

	echo "<br><br>JSON data put back into original JSON file...<br><br>";
	file_put_contents($file, $json);
?>
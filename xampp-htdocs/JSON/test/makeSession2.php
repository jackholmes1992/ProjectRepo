<?php
$jsonData = new stdClass();
$session = array(
/*	array(
	'sessionId' => '000000',
	'sessionName' => 'deathFolkPopJam',
	'sessionCreator' => 'Jack'
	),*/
	array(
		'clipId' => '000000',
		'position' => '00.00.00.00',
		'creator' => 'Jack'
	),
	array(
		'clipId' => '111111',
		'position' => '00.00.00.00',
		'creator' => 'Toby'
	),
	array(
		'clipId' => '222222',
		'position' => '00.00.00.00',
		'creator' => 'Keith'
	)
);

//$jsonData->source = "Program knowledge";
//$jsonData->published = date('Y-m-d H:s:i');
//$jsonData->status = true;
$jsonData->session = $session;
$JSON = json_encode($jsonData);

file_put_contents('Session2.json', $JSON);
?>
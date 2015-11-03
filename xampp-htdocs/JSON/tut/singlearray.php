<?php
	$mobiles = array('Samsung', 'Apple', 'Nokia', 'Sony', 'LG');
	$jsonMobiles = json_encode($mobiles);

	echo $jsonMobiles;
	// Output:-
	// ["Samsung","Apple","Nokia","Sony","LG"]


	$phpMobiles = json_decode($jsonMobiles);
	print_r($phpMobiles);
 	// Output:-
	// Array ( [0] => Samsung [1] => Apple [2] => Nokia [3] => Sony [4] => LG ) 

	//save to a seperate JSON file
	$jsonMobiles = json_encode($mobiles);
	file_put_contents('mobiles.json', $jsonMobiles);

?>
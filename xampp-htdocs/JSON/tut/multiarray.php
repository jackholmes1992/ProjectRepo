<?php
	//encoding to JSON
	$products = array(
					'name'	=> 'Mukesh Chapagain',
					'address'	=> 'Kathmandu, Nepal',
					'website'	=> 'http://blog.chapagain.com.np',
					'mobiles' 	=> array('Samsung', 'Apple', 'Nokia', 'Sony', 'LG'),
					'furniture' => array('Chair', 'Couch', 'Ottoman'),
					'camera'	=> array('Canon', 'Nikon')
				);
	$jsonProducts = json_encode($products);
	echo $jsonProducts;
	echo "<br><br><br>";
?>


<?php
	//decoding JSON to variables
	$phpProducts = json_decode($jsonProducts);
	print_r($phpProducts);
	echo "<br><br><br>";
	 
	// printing name, address, and website
	echo "Name: " . $phpProducts->name . "<br />";
	echo "Address: " . $phpProducts->address . "<br />";
	echo "Website: " . $phpProducts->website . "<br />";
 
	// printing mobiles name
	foreach ($phpProducts->mobiles as $key => $value) {	
		echo $value . "<br />";
	}
?>


<?php
	//write to a new JSON file
	$jsonProducts = json_encode($products);
	file_put_contents('products.json', $jsonProducts);
?>
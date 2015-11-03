<?php
	$jsondata = file_get_contents("movies.json");
	$json = json_decode($jsondata,true);
	echo $json['movies'][0]['title']; //print first title in list
	echo "<br><br><br>";
	
	$output  = "<ul>";
	foreach($json['movies'] as $movie){
		$output .= "<h4>".$movie['title']."</h4>";
		$output .= "<li>".$movie['year']."</li>";
		$output .= "<li>".$movie['genre']."</li>";
		$output .= "<li>".$movie['director']."</li>";
	}
	$output .= "</ul>";
	echo $output;
?>
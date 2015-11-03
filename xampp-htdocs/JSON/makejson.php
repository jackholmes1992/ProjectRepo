<?php
$jsonData = new stdClass();
$movies = array(
	array(
		'title' => 'Inception',
		'year' => '2013',
		'genre' => 'Action',
		'director' => 'Christopher Nolan'
	),
	array(
		'title' => 'Spectre',
		'year' => '2015',
		'genre' => 'Action',
		'director' => 'Sam Mendes'
	),
	array(
		'title' => 'Interstellar',
		'year' => '2014',
		'genre' => 'Sci-fi',
		'director' => 'Christopher Nolan'
	)
);

//$jsonData->source = "Program knowledge";
//$jsonData->published = date('Y-m-d H:s:i');
//$jsonData->status = true;
$jsonData->movies = $movies;
$JSON = json_encode($jsonData);

file_put_contents('films.json', $JSON);
?>
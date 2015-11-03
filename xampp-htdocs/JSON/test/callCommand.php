<?php

	//exec() -- which can store the output of the command in an array
	//shell_exec() -- which returns, as a string, the output of the command
	//system() -- which echoes the output of the command
	

	$newClipId = '111111';
	$clip1Id = 'Skid';
	$clip2Id = 'PropellerEngine';
	
	exec("./sox -M ".$clip1Id.".wav ".$clip2Id.".wav ".$newClipId.".wav");
	//system("ls");

?>
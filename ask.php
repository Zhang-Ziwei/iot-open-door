<?php
$param = $_GET["chstat"];
$file = "stat.txt";

if($param == "o"){	//ask stat and write 
	echo file_get_contents($file);
	file_put_contents($file, "1");
}
if($param == "c"){	//ask stat and write 
	echo file_get_contents($file);
	file_put_contents($file, "0");
}
if($param == "a"){	//ask stat and write 2
	echo file_get_contents($file);
	file_put_contents($file, "2");
}
?>

 <!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/Downloadcss.css">
<style>
.center {
  text-align: left;
  border: 3px solid green;
  padding: 35px 50px;
  font-size: 20px;
}

</style>
</head>
<body>

<h2 style="text-align:center;">Summary</h2>

<div class="center">
  <p><?php

$command_exec = escapeshellcmd('python C:/xampp/htdocs/BE_Project/BE_Project/text_summarization.py 2>&1');
$str_output = shell_exec($command_exec);
#echo $str_output;
#echo "<br>";

$myFile = "C:/xampp/htdocs/BE_Project/BE_Project/summary.txt";
$fh = fopen($myFile, 'r') or die("Unable to open file!");
echo fread($fh,filesize($myFile));
fclose($fh);


?>  </p>
</div>
<center>
<!--<a id="download_link" download="F:\Python_projects\summary.txt" href=”” >Download as Text File</a>-->
<a href="summary.txt" download>Download Summary Now</a>
</center>
</body>
</html>

<?php

?>

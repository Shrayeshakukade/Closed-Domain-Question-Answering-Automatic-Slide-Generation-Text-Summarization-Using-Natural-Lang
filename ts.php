<?php
if(array_key_exists('button1', $_POST)) {
    button2();
}
#function button1() {
#    $command_exec = escapeshellcmd('python F:\Python_projects\examine.py');
#    $str_output = shell_exec($command_exec);
#    echo $str_output;
#}
function button2() {
  header("Location:demo.php");
}



?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
    <title>Text Summarization</title>

    <!-- CSS  -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
<body>
<div class="navbar-fixed">
  <nav class="teal">
        <div class="container">
            <div class="nav-wrapper">
                <a href="#" class="brand-logo white-text">Text-Summarization Portal</a>
                
                </a>
                <ul class="right hide-on-med-and-down">
                <li>
                     <a href="#home" class="white-text">Home</a>
                </li>
                 <li>
                     <a href="#search" class="white-text">Search</a>
                </li>
                <li>
                    <a href="#answer" class="white-text">Answer</a>
                </li>
                <li>
                    <a href="#contact" class="white-text">Contact</a>
                </li>
                </ul>
            </div>
        </div>
  </nav>
</div>
<div class="fixed-action-btn">
<a href="#" class="btn-floating red btn-large"><i class="large material-icons">apps</i></a>
<ul>
<li><a href="index1.html" class="btn-floating purple btn-large"><i class="large material-icons">account_balance</i></a>
<li><a href="contactUs.html" class="btn-floating blue btn-large"><i class="large material-icons">chat</i></a>
<li><a href="Services.html" class="btn-floating green btn-large"><i class="large material-icons">dashboard</i></a>
<li><a href="ReadMore.html" class="btn-floating orange btn-large"><i class="large material-icons">description</i></a>



</div>
<section class="slider">
    <ul class="slides">
      <li>
        <img src="images/parallax1.jpg"> <!-- random image -->
        <div class="caption center-align">
          <h2>Select a Pdf or Text file</h2>
          <h5 class="light grey-text text-lighten-3 hide-on-small-only">To get the summarized form of pdf</h5>
        </div>
      </li>
      <li>
        <img src="images/parallax2.jpg"> <!-- random image -->
        <div class="caption left-align">
          <h2>Upload the File</h2>
          <h5 class="light grey-text text-lighten-3 hide-on-small-only ">Click on upload button</h5>
        </div>
      </li>
      <li>
        <img src="images/sample-1.jpg"> <!-- random image -->
        <div class="caption right-align">
          <h2>Get the summarization</h2>
          <h5 class="light grey-text text-lighten-3">Please wait till your summary is generated</h5>
        </div>
      </li>
    </ul>

</section>
<div class="container">
   <div class="card-panel">
   	<form action="?" method="POST" enctype="multipart/form-data">
    <label>Please select a File</label>

 
	<div class="file-field input-field">
		<div class="btn ">
			<span>FILE</span><p><input type="file" name="file"> </p>

		</div>

		<div class="file-path-wrapper">
			<input type="text" class="file-path">
		</div>
	</div>
	<p><input type="submit" name="upload" value="upload" class="btn right"></p>
		<div class="clearfix"></div>
	
    <?php
set_time_limit(500);
error_reporting(E_ERROR | E_PARSE);
if(isset($_POST['upload'])){
      $directory = "C:/xampp/htdocs/BE_Project/BE_Project/upload_files/";
      $files = scandir ($directory);
      $firstFile = $directory . $files[2];
      unlink($firstFile);
      $file = $_FILES['file'];
      $fileName = $_FILES['file']['name'];
      $fileTmpLoc = $_FILES['file']['tmp_name'];
      $fileSize = $_FILES['file']['size'];
      $fileType = $_FILES['file']['type'];
      $fileError = $_FILES['file']['error'];

      $fileExt = explode('.',$fileName);
      $fileActualExt = strtolower(end($fileExt));
      
      $allowed = array('pdf');

      if(in_array($fileActualExt, $allowed)){
          if($fileError === 0){
              if($fileSize < 157286400){
                  #$fileNameNew = uniqid('',true).".".$fileActualExt;
                  $fileDestination = 'upload_files/'.$fileName;
                  if (move_uploaded_file($fileTmpLoc, $fileDestination)){
                    ?>
                    <div  class="alert alert-success">
                    <?php
                              echo "File Uploaded Successfully";
                    ?>
                    </div>
                  <?php
              }
          }else{
              echo "Your file is too big";
          }
      }else{
          echo "There was an error uploading your file";
      }
  }else{
      echo "You cannot upload files of this type";
  }
}
?>


   <!-- <p><input type="submit" name="upload" value="Upload Image"></p>-->
 <p class="center-align">
    <input type="submit" name="button1" class="btn-large" value="Generate Summary"></p>
<div class="clearfix"></div>

</div> 
</div>
<section class="section section-icons grey lighten-4 center">
    <div class="container">
    <div class="row">
    <div class="col s12 m4">
    <div class="card-panel">
    <i class="material-icons large teal-text">search</i>
    <h4>Select a File</h4>
    <p>Select a File from the dropdown menu
    </p>
    </div>
    </div>
    <div class="col s12 m4">
    <div class="card-panel">
    <i class="material-icons large teal-text">file_upload</i>
    <h4>Upload the file</h4>
    <p>Click on the upload button to give the file as an input
    </p>
    </div>
    </div>
    <div class="col s12 m4">
    <div class="card-panel">
    <i class="material-icons large teal-text">question_answer</i>
    <h4>Get your Summary</h4>
    <p>The summary will be generated
    </p>
    </div>
    </div>
</section>  

<!--  Scripts-->
<script src="js/jquery-2.1.1.min.js"></script>
<script src="js/materialize.js"></script>
<script src="js/init.js"></script>
<script src="js/eventsource.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js"></script>
<script>
    const slider=document.querySelector('.slider');
    M.Slider.init(slider,{indicators:false,height:500,transition:500,interval:6000});
</script>
</body>
</html>

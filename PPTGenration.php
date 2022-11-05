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
                <a href="#" class="brand-logo white-text">Presentation Slides Generation Portal</a>
                
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
          <h5 class="light grey-text text-lighten-3 hide-on-small-only">To generate the ppt</h5>
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
          <h2>Get the Slides</h2>
          <h5 class="light grey-text text-lighten-3">Please wait till your ppt gets downloaded</h5>
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
			<input type="text" name="input_path" class="file-path">
		</div>
	</div>
	<p><input type="submit" name="upload" value="upload" class="btn right"></p>
		<div class="clearfix"></div>
	
    

<?php

    if(isset($_POST['upload']))
    {
        $file_name = $_FILES['file']['name'];
        $file_type = $_FILES['file']['type'];
        $file_size = $_FILES['file']['size'];
        $file_tem_loc = $_FILES['file']['tmp_name'];
        $file_store = "upload/".$file_name;

        if(move_uploaded_file($file_tem_loc,$file_store))
        {
?>
	<div  class="alert alert-success">
	<?php
            echo "File Uploaded Successfully";
	?>
	</div>
<?php
        }
    }
?>

   <!-- <p><input type="submit" name="upload" value="Upload Image"></p>-->
<div class="input-field">
<input type="text" name="title" id="titleforslides">
<label for="titleforslides">Enter a title for the PPT</label>
</div>
 <p class="center-align">
    <input type="submit" name="button1" class="btn-large" value="Generate PPT"></p>
<div class="clearfix"></div>
<?php
if(array_key_exists('button1', $_POST)) {

  button2();

}
function button2() {

  $title=$_POST['title']; 
  $input_path=$_POST['input_path'];
  echo $title; 
  #echo $file_store;
  $output_path_download = 'C:\Users\kukad\Downloads\generated';
  $process_status = 1;
  #echo $process_status;
  #exec('python "/site/pyt/Script.py" "'.$arg.'"', $output, $return_var);

  #$command_exec = escapeshellcmd("python C:/xampp/htdocs/Newfolde/driver.py -I $input_path -O $output_path_download -T $title -P $process_status");
  


  #$command_exec = escapeshellcmd("python driver.py -I upload/sample.pdf -O C:/Users/kukad/Downloads/generated -T cloudcomputing -P 1");
  #$str_output = shell_exec($command_exec);
  $command = "python C:/xampp/htdocs/Newfolder/driver.py -I {$input_path} -O {$output_path_download} -T {$title} -P 1 2>&1";
  #$command = "python C:/xampp/htdocs/Newfolder/new.py"
  $command = escapeshellcmd($command);
  #escapeshellcmd($command);
  shell_exec($command);
  #shell_exec("python driver.py -I upload\sample.pdf -O C:\Users\kukad\Downloads\generated -T cloudcomputing -P 1");
  #echo $str_output;
  echo "<br>";
  echo "ppt generated";
}

  
?>
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
    <i class="material-icons large teal-text">view_day</i>
    <h4>Get your PPT</h4>
    <p>The ppt will be downloaded
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

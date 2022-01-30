<!DOCTYPE html>

<?php 
	include 'datastruct.php';
	include 'crawler.php';
	
	session_start();

	if(!isset($_SESSION["crawler"]))
	{
		$_SESSION["crawler"] =  unserialize(file_get_contents('crawler'));
	}
	if(!isset($_SESSION["searcher"]))
	{
		$_SESSION["searcher"] = unserialize(file_get_contents('searcher'));
	}

?>

<html>
	<head>
		<link type="text/css"
				rel="stylesheet"
				href="style.css"/>
		
	</head>
	
	<body>
		<div class="container">
			<form action="index.php" method="get">
				<img src="johnlogo.jpg"
					width="500"
					height="300"/>
					
				<div class="search">
				
					<?php
						if( isset($_GET["query"]))
						{
							echo '<input 	type="text" 
											name="query" 
											maxlength="255" 
											size="64" 
											value="'.$_GET["query"].'" 
											x-webkit-speech/>';
						}
						else
						{
							echo '<input 	type="text" 
											name="query" 
											maxlength="255" 
											size="64" 
											x-webkit-speech/>';
						}
					?>
					
					<br/>
					<input type="submit" value="Search" />
				</div>
			</form>	
			
			<?php
				if(isset($_GET["query"]))
				{
					$start = microtime(true);
					
					
										
					$results = $_SESSION["searcher"]->Search( sanitizeQuery($_GET["query"]) );
					
					$totalTime = number_format( (microtime(true)-$start), 3);
					
					if( count($results) == 0 )
					{
						echo "<p class=\"warning\">Sorry, your query yields no results</p>";
					}
					else if( count($results) == 1)
					{
						echo "<p class=\"message\"> Displaying your result in ".$totalTime." seconds. </p>";
					}
					else if( count($results > 1 ) )
					{
										
						echo "<p class=\"message\"> Displaying ". count($results) . " results in " . $totalTime . " seconds. </p>";
					}
					displayResults($results, $_SESSION["crawler"]->crawledPages);
					
					
				}
			?>
			<div class="footer">
				Created by Johnathan Pelz and John Gibbons. Copyright 2012.
			</div>
		</div><!-- End container -->
		
	</body>
</html>

<?php
	function displayResults($results, $lookup)
	{		
		echo"<div class='resultlist'>";
		
		foreach($results as $filename => $score)
		{
			$score = number_format( $score, 4);
			echo"
					<div class='result'> 
						<div class='score'>$score</div> <a href='".$lookup[$filename]."' target='_blank'>".$lookup[$filename]."  </a>
					</div><!-- result -->";
		}
		echo"</div><!-- resultlist -->";
	}
?>

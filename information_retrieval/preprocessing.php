<?php
	include 'datastruct.php';
	include 'crawler.php';

	$start = microtime(true);

	$searcher = new InvertedIndex();
	$crawler = new Crawler();
	$dirName = "docs";
	
	$dir = opendir($dirName);
	//empty the directory in preparation for new documents
	
	while (false !== ($entry = readdir($dir))) 
	{
		if(	"." != $entry && ".." != $entry)
		{
			unlink("$dirName/".$entry);
		}
	}

	
	//Crawl pages
	$crawler->seed = "http://eecs.ku.edu";
	$crawler->maxDepth = 10;
	$crawler->maxPages = 500;
	$crawler->domain = "eecs.ku.edu";
	$crawler->dir = "$dirName/"; //all files will be stored in the docs directory.  Make sure it's created before crawling
	@$crawler->crawl();
	
	$numPagesCrawled = count($crawler->crawledPages);
	$domain = $crawler->domain;
	file_put_contents("crawler", serialize($crawler));
	unset($crawler);
	
	
	
	rewinddir($dir);

			
	//Page rank all documents
	while (false !== ($entry = readdir($dir))) 
	{
		if(	"." != $entry && 
			".." != $entry  && 
			preg_match('#html*?#',$entry) >0)
		{		
			//echo "analyzing $entry <br/>";
			$searcher->ConstructDictionary($entry, sanitize("$dirName/".$entry));
		}   
	}
	

	
	closedir($dir);	
	
	
	
	file_put_contents("searcher",serialize($searcher));
	
	$totalTime = number_format( (microtime(true)-$start), 3);
	
	echo "<h1> Preprocessing finished</h1>";
	echo $numPagesCrawled . " collected and indexed from " . $domain .  " in " . number_format( (microtime(true)-$start), 3) . " seconds <br/>";
	
	
	
	
?>
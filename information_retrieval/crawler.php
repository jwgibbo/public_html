<?php

class Crawler
{
	public $seed;			//Starting point of crawling
	public $domain;			//Domain of the starting point
	public $dir;			//Directory to store files
	public $maxDepth; 		//Depth the crawler is allow to go
	public $maxPages; 		//Number of pages allowed to download
	public $crawledPages;	//Dictionary of fileNames=>urls that have been crawled
	public $sleepTime;		//Seconds between downloads
	
	public function __construct()
	{
		$this->seed = "";
		$this->dir = ""; //puts files in current working directory by default
		$this->maxDepth = 1; //default depth of 1
		$this->maxPages = 1000;//default to collecting only 1000 pages
		$this->sleepTime = 2;//Seconds between downloads
		$this->crawledPages = array(); 
	}
	
	/*
		stores the HTML code of $url in file $fileName inside directory $dir.
	*/
	public function storeURL($url, $fileName, $dir='')
	{

		$data = file_get_contents($url);
		
		file_put_contents($dir.$fileName, $data);

	}


	/*
		Takes string, $url, representing a URL.  e.g. http://wikipedia.com/article
		Returns a string, that is a safe file name.  
			http:// replaced with ''
			www replaced with ''
			/ are replaced with _ (underscore)
			? are replaced with ''
			& are replaced with ''
			= are replaced with ''
			% are replaced with ''
			
			an extension of .html is added.
			
			Example:
			$url = "http://wikipedia.com/article"
			value returned ==> "wikipedia.com_article.html"
	*/
	
	public function urlToFileName($url)
	{
		$tokensToRemove = array("http://", "www.", "/", "?", "&", "=", "%");
		return(str_replace($tokensToRemove, array('', '', '_', '', '', '', ''), $url).".html");
	}

	/*
		$html is a string of valid html code.
		$domain is the full domain  e.g. wikipedia.org or amazon.com
		Returns an array with all urls for out going links.
	*/	
	
	public function outGoingLinks($html, $domain="")
	{
		
		$pattern = '#a\s+href\s*="([\w/]*)"#'; //NOTE: links to subsections (e.g. table on contents in wikipedia) are ignored. 
		$replacement = '$2 ';//grab only the URL
		
		/* preg_match_all will create a 2D array. 
			$matches[0] is an array with all matching patterns
			$matches[1] is an array with just the URLs
		*/
		
		preg_match_all($pattern, $html, $matches);
		
		/*Examine all outgoing URLs and ensure any relative URLs are converted to absolute URLs.
			e.g. convert /wiki/article to http://wikipedia.org/wiki/article */
		
		
		foreach( $matches[1] as $index => $url )
		{
			// if a url is not absolute
			if( preg_match("#http:\/\/#", $url) == 0 )
			{
				if( $domain != "" )
				{
					// if the url needs a preceeding / place it
					if( substr($url,0,1) != '/' )
					{
						$matches[1][$index] = "http://".$domain.'/'.$url;
					}
					else
					{			
						$matches[1][$index] =  "http://".$domain.$url;
					}
				}
				else
				{
					echo "<b><p>relative URL detected, but no domain given to outGoingLinks()</p></b>";
				}
			}
		} 
		return ($matches[1]);
	}

	/* 
		$frontier is an array of URLs
		recursive version of crawl()
		all files are downloaded and stored locally to $this->dir
	*/
	public function recCrawl($frontier, $curDepth=1)
	{
		if($curDepth <= $this->maxDepth && count($this->crawledPages) <= $this->maxPages)
		{
			//download all the files in the frontier and store them locally
			foreach( $frontier as $index => $link )
			{
				//If the page has not been crawled
				if(!in_array($link, $this->crawledPages))
				{
					$fileName = $this->urlToFileName($link);
						
					$this->storeURL($link, $fileName, $this->dir);	
					
					$this->crawledPages[$fileName] = $link;//store the url and local file name in crawled pages
					
					//echo "Storing $link in $fileName.  Current depth $curDepth <br/>";				
					
					// sleep for 0.1 seconds
					time_nanosleep(0, 500000000*$this->sleepTime);
					
					//get all outgoing links and add them to the frontier
					//The @ in front of file_get_contents supresses warnings from 403/404 errors.
					@$this->recCrawl($this->outGoingLinks(file_get_contents($link), $this->domain), $curDepth+1);	

					
				}				
			}	
		}
	}

	
	public function crawl()
	{
		$curDepth = 1;
		$curFrontier = array($this->seed);//Array to contain the URLs in the frontier
		$nextFrontier = array();//empty array because we need to crawl the current frontier to discover the next frontier
		file_put_contents("crawledList.txt", "");
		while( $curDepth <= $this->maxDepth )
		{
			
			
			foreach($curFrontier as $index => $url)
			{
				if(count($this->crawledPages) < $this->maxPages)
				{
					$fileName = $this->urlToFileName($url);//create a file name from the url
					
					if(!isset($this->crawledPages[$fileName]))
					{
						$this->storeURL($url, $fileName, $this->dir);//download the url
					
						$this->crawledPages[$fileName] = $url;//store the url and local file name in crawled pages
					
						file_put_contents("crawledList.txt", $url."\t".memory_get_usage()."\n",FILE_APPEND);
					
						// sleep for 0.1 seconds
						//time_nanosleep(0, 100000000);
						if( count($this->crawledPages) + count($curFrontier) < $this->maxPages )
						{
							$nextFrontier = array_merge($nextFrontier, $this->outGoingLinks(file_get_contents($url), $this->domain));				
						}
						else
						{
							unset($nextFrontier);
							$nextFrontier = array();
						}
					}
				}
				else
				{
					break;
				}
				
				
			}
			
			unset($curFrontier);
			$curFrontier = array();
			
			$curFrontier = $nextFrontier;
			
			unset($nextFrontier);
			$nextFrontier = array();
			
			$curDepth++;				
		}		
		file_put_contents("crawledList.txt", "crawler finished\t".memory_get_usage()."\n",FILE_APPEND);
	}
}



?>
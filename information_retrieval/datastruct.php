<?php
// EECS 767
// Project 1
// John, Johnathan

include 'sanitizer.php';

class InvertedIndex
{
	private $Dictionary;
	private $docCount;
	private $similarities; 

	
	public function __construct()
	{
  	  $this->Dictionary = Array();
	  $this->similarities = Array();
	}

	public function ConstructDictionary($documentID, $tokens)
	{
  	  foreach($tokens as $term)
  	  {
  		  // already exists update term.
  		  if(isset($this->Dictionary[$term]))
  		  {
  			  $tempFreqInfo = $this->Dictionary[$term];
  			  // update docFreq only if document hasn't been used.
  			  if(!$tempFreqInfo->ContainsDocumentID($documentID))
  				  $tempFreqInfo->IncromentDocFreq();
  			 
  			  // update term Freq
  			  $tempFreqInfo->IncromentTermFreq();
  			 
  			  // update Postings!
  			  $tempFreqInfo->UpdatePosting($documentID);
  		 
  			  // write back freqInfo
  			  $this->Dictionary[$term] = $tempFreqInfo;
  		  }
  		  else
  		  { // Not in dictionary
  			 
  			  $newTerm = new FreqInfo();
  			  // add posting
  			  $newTerm->UpdatePosting($documentID);
  			  // write back to dictionary
  			  $this->Dictionary[$term] = $newTerm;
  		  }
  	  }
	  
	  $this->similarities[$documentID] = -1;
	}
    
	public function GetVectorLength( $v )
	{
		$sum =  0;
		
		foreach ( $v as $term => $value )
		{
			$sum = $sum + pow($value, 2);
		}
		
		return( sqrt($sum) );
	}

	public function GenerateQueryVector( $terms )
	{
		$queryVector = Array();

		//Create a vector of size #terms		
		foreach( $terms as $term )
		{
			if( isset($this->Dictionary[$term] ) )
			{
				$queryVector[$term] = $this->Dictionary[$term]->GetIDF( count($this->similarities) );
			}	
		}

		return ($queryVector);
	}
	
	
	public function GenerateDocVector( $docID )
	{
		$tempDocVector = Array();
		$freqText ="";
		$idfText="";
		$tfidfText="";
		foreach( $this->Dictionary as $term => $freqInfo )
		{
			if( isset($freqInfo->Postings[$docID] ) )
			{
				$tempDocVector[$term] = $freqInfo->Postings[$docID]->GetTermFreq() * $freqInfo->GetIDF( count($this->similarities) );
				$freqText .= $docID . "==>" . $freqInfo->Postings[$docID]->GetTermFreq() . "\n";
				$idfText .= $freqInfo->GetIDF( count($this->similarities) ) . "\n";
				$tfidfText .= $term . "==>" .$tempDocVector[$term] . "\n";
			}
		}

		return($tempDocVector);
	}
	
	
	public function CreateSimilarities($queryTerms)
	{
		$queryVector = Array();
		$tempDocVector = Array();
		
		$queryVector = $this->GenerateQueryVector($queryTerms);
			
		foreach( $this->similarities as $docID => $sim )
		{
			$tempDocVector = $this->GenerateDocVector($docID);
			
			if( count($queryVector) < count($tempDocVector) )
			{
				$dotProduct = 0;
				foreach($queryVector as $term => $value)
				{
					if(isset($tempDocVector[$term]))
					{
						$dotProduct += $value * $tempDocVector[$term];
					}			
				}
			}
			else
			{
				$dotProduct = 0;
				foreach($tempDocVector as $term => $value)
				{
					if(isset($queryVector[$term]))
					{
						$dotProduct += $value * $queryVector[$term];
					}
				}
			}
			
			$queryVectorLength = $this->GetVectorLength($queryVector);
			$docVectorLength = $this->GetVectorLength($tempDocVector);
			
			if( $queryVectorLength == 0 || $docVectorLength == 0 )
			{
				$this->similarities[$docID] = 0;
			}
			else
			{
				$this->similarities[$docID] = $dotProduct / ( $queryVectorLength * $docVectorLength );
			}
			
			unset($tempDocVector);
			$tempDocVector = Array();
		}
	}
	
	public function Search($arrayOfTerms)
	{ // Returns an ArrayObject of documents which contains one of the terms
		$result = array();
		
		$queryTermsNotInDictionary = array_diff( $arrayOfTerms, array_keys($this->Dictionary));
		
		//Only look for similarities if at least one of the query terms is in the dictionary
		if( count( $queryTermsNotInDictionary ) < count( $arrayOfTerms ) )
		{
			//pull out the query terms that are in the dictionary
			$validTerms = array_diff($arrayOfTerms, $queryTermsNotInDictionary);
			
			$this->CreateSimilarities($validTerms);

			//Sort similarities by term frequency

			asort( $this->similarities, SORT_NUMERIC );

			foreach($this->similarities as $docID => $sim)
			{
				if($sim > 0)
				{
					$result[$docID] = $sim;
				}
			}
		}
		
		return (array_reverse($result));
	}
	
}



class FreqInfo
{
	private $DocFreq;   	 
	private $TermFreq;  	 
	public $Postings;  	 
    
	
	
	public function __construct()
	{
  	  $this->DocFreq = 1;
  	  $this->TermFreq = 1;
  	  $this->Postings = new ArrayObject();
	}
    
	public function GetIDF( $numDocs )
	{
		return( log10( $numDocs / $this->DocFreq) );
	}
	
	public function GetPostings()
	{
  	  return $this->Postings;
	}
	public function GetTermFreq()
	{
  	  return $this->TermFreq;
	}
	public function GetDocumentFreq()
	{
  	  return $this->DocFreq;
	}
    
	public function IncromentDocFreq()
	{    
  	  $this->DocFreq++;
	}
    
	public function IncromentTermFreq()
	{
  	  $this->TermFreq++;
	}
    
	public function ContainsDocumentID($documentID)
	{
  	  return (isset($this->Postings[$documentID]));
	}
    
	public function GetDocuments()
	{
  	  $result = array();
  	  foreach($this->Postings as $post)
  	  {
  		  array_push($result, $post->GetDocumentID());
  	  }
  	  return $result;
	}
    
	public function UpdatePosting($documentID)
	{	// Create or update a given posting based on $documentID
  	  if(isset($this->Postings[$documentID]))
  	  {
  		  $this->Postings[$documentID]->IncromentTermFreq();
  	  }
  	  else
  	  {
  		  $newPost = new Posting($documentID);
  		  $this->Postings[$documentID] = $newPost;
  	  }
	}
}



class Posting
{
	private $DocID;
	private $TermFreq;
    
	public function __construct($DocID_FileName)
	{
  	  $this->DocID = $DocID_FileName;
  	  $this->TermFreq = 1;
	}
    
	public function IncromentTermFreq()
	{
  	  $this->TermFreq++;
	}
    
	public function GetDocumentID()
	{
  	  return $this->DocID;
	}

	public function GetDocuments()
	{
  	  return $this->Postings;
	}
	public function GetTermFreq()
	{
  	  return $this->TermFreq;
	}
}



?>
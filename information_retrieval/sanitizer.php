<?php

//Test output of what sanitize returns.
//recPrint(sanitize("docs/Acadia_National_Park.htm"));

/*
	Debug function for finding ascii codes for unusual characters.
*/
function asciiPrint()
{
	for($i=0; $i<256; $i++)
	{
											
		echo "$i => " . chr($i) . "<br/>";
	}
}
	//testHandler();

/*
	*Handles the replacing or removing of special characters.
	*$string is any valid string
	*Returns a string with removed/replaced characters.
*/
function handleSpecialCharacters( $string )
{
	$oddHyphen = chr(150);
	
	$pattern = array( 	'#\&\#\S+;#i',
						'#(\D)(\.)(\D)#i',
						'#(\D)(\:)(\D)#i',
						'#\;#i',
						'#\?#i',
						'#/#i',
						'#`#i',
						'#\'#i',
						'#\"#i',
						'#(\D|\s)(,)(\D|\s)#i',
						'#\d,\d#i',
						'#~#i',
						'#(\w)(!)#i',
						'#@#i',
						'#&#i',
						'#\(#i',
						'#\)#i',
						'#-#i',
						'#_#i',
						'#(\s)(\+)(\s)#i',
						'#(\w)(\+)(\w)#i',
						'#\[#i',
						'#\]#i',
						'#\{#',
						'#\}#',
						'#'.$oddHyphen.'#i',
						'#°#i');
						
	$replacement = array(	' ',  		/* replace HTML character codes with space */
							'$1 $3',  /* period to space, keep any characters touching it*/
							'$1 $3',  /* colon to space, keep any characters touching it*/
							' ',		/*semi-colon to space */	
							' ',		/* question mark to space */
							' ',		/* forward slash to space */
							'',			/* ` removed */
							'',			/* ' removed */
							' ',		/* " replaced with space */
							'$1 $3',		/* , touching letters or white space replaced with space */
							'', 		/* , touching numbers removed */
							'',			/* ~ removed */
							'$1 ', 		/* remove ! at end of token */
							' ',		/* @ to space */
							' ',		/* & to space */
							' ',		/* ( to space */
							' ',		/* ) to space */
							' ',		/* - to space */
							' ',		/* _ to space */
							' ',  		/* + to space */
							' ',		/* + to space */
							' ',		/* [ to space */
							' ',		/* ] to space */
							' ',		/* { to space */
							' ',		/* } to space*/
							' ',		/* odd hyphen to space */
							' ');		/* ° (degree to space) */
	
	$string = preg_replace($pattern, $replacement, $string);
	
	return ($string);
}





/*
	* Recursively prints an array or object's members and values
	* $data is an object or array
	* return nothing
	* Note: useful debugging tool
*/
function recPrint($data)
{
	if( is_array( $data ) || is_object($data) )
	{
		foreach($data as $key => $value)
		{
			echo "$key => ";
			recPrint( $value );
			echo "<br/>";
		}
	}
	else
	{
		if($data == "")
		{
			echo "NULL";
		}
		else
		{
			echo "$data";
		}
	}
}




/*
	Coverts an HTML file to an array of sanitized tokens
*/
function sanitize($htmlFileName)
{
	$tokens = array();
	
	
	$htmlCode = file_get_contents($htmlFileName);
	$htmlCode = stripSpecialTags($htmlCode);
	$text = strip_tags($htmlCode);	
	$text = handleSpecialCharacters($text);
	$text = strtolower($text);
	
	//Turn sanitized string into an array of tokens
	
	$splitPattern = "#\s#i";
	$tokens = preg_split($splitPattern, $text);

	//Remove any NULL or empty strings	
	$tokens = array_diff($tokens, array(NULL,""));
	
	return($tokens);
}


/*
	Coverts a string to an array of sanitized tokens
*/
function sanitizeQuery($str)
{

	$tokens = array();

	$str = strip_tags($str);	
	$str = handleSpecialCharacters($str);
	$str = strtolower($str);
	
	
	
	
	//Turn sanitized string into an array of tokens
	
	$splitPattern = "#\s#i";
	$tokens = preg_split($splitPattern, $str);

	//Remove any NULL, and, or empty strings	
	$tokens = array_diff($tokens, array(NULL,"", "and"));
	
	return($tokens);
}

/*
	$string is any valid string
	
	Returns: A string with the <script> and/or <style> with all inner javascript or css removed
*/
function stripSpecialTags($string)
{
	$pattern = array( '#<script[^>]*>[^<]*</script>#i',
						'#<style[^>]*>[^<]*</style>#i');
						
	$replacement = array('','');
	
	return(preg_replace($pattern, $replacement, $string));
}



/*
	*simple test function to verify the proper handling of special characters
*/
function testHandler()
{
	$test = " 3.1415 facebook.com <br/> 
			5:1 derp: herp <br/>
			asdf; asdf;asdf; ;; asdf; <br/>
			asdf? asdf? asdf? asdf?? <br/>
			asdf/as f/asdf/asfd/f f/ f/sf  as/f/ <br/>
			asdf`s a `sfdasdf `sadf` `fsfd` asdf`<br/>
			hgf~jhgf ~~  ~~~~ hgfjhf~ hGF~hj sadf~dsf H~Gf <br/>
			!= asdf! <br/>
			derp@herp.com <br/>
			Sanford&son & others<br/>
			Math (which is cool) has numbers (3+2)/3=1 <br/>
			smith-martinez 4-3=1 <br/>
			file_name.exe _members_ _ _ _ _ <br/>
			5 + 1 C++ <br/>
			if{(x=1) then do stuff} <br/>
			Asticou's Island Domain: Wabanaki Peoples at Mount Desert Island 1500–2000 (2007)";

			
	echo handleSpecialCharacters ($test);
}
 
?>
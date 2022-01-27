#include <iostream>

#include "SomeClass.h"
#include "AnotherClass.h"

int main()
{
	SomeClass someClassObject(5);
	
	std::string word1 = "banana";
	std::string word2 = "bananas";
	std::string word3 = "bananarama";
	
		
	someClassObject.interactWithData(AnotherClass::printAnInt);

	return(0);
}
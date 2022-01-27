#include <iostream>

#include "SomeClass.h"
#include "AnotherClass.h"

int main()
{
	SomeClass someClassObject(5);
		
	someClassObject.interactWithData(AnotherClass::printAnInt);

	return(0);
}
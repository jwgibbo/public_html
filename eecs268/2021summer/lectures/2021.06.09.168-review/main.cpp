#include <iostream>

#include "Account.h"

int main()
{
	Account myAccount(100);
	
	//Draw the call stack and heap
	Account* yourAccount = nullptr;
	
	yourAccount = new Account(50);
	
	delete yourAccount;
	
	return(0);
}
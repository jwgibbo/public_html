#include <iostream>
#include "Account.h"
#include <string>

int main()
{
	//This doesn't work because we can't pass in
	//the required parameter to each constructor
	//call
	// Account* bank = new Account[5];
	
	//Instead, we'll create an array of Account pointers
	Account** bank = nullptr;
	int numAccounts = 4;
	
	bank = new Account*[ numAccounts ];
	
	for(int i=0; i<numAccounts; i++)
	{
		bank[i] = new Account(5);
	}
	
	return(0);
}




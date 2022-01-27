#include <iostream>
#include "Account.h"

int main()
{
	//Stack allocated objects
	Account myAccount(100);
	Account yourAccount;
	
	yourAccount.deposit(5);
	

	//Heap allocated account objects
	Account* accountPtr = nullptr;
	
	//allocate the object
	accountPtr = new Account();
	
	(*accountPtr).deposit(5);
	
	accountPtr->deposit(5);
	
	delete accountPtr;
	
	return(0);
}




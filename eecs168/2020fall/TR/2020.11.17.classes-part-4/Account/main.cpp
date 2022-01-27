//main.cpp
#include <iostream>
#include "Account.h"


int main()
{
	Account myAccount(51); //constructor is called
	Account yourAccount(50); //constructor is called
	
	//Declare an Account pointer
	Account* accountPtr = nullptr;
	
	//create the heap allocated object
	accountPtr = new Account(25);
	
	// instead of doing...
	//(*accountPtr).deposit(100);
	accountPtr->deposit(100);
	
	std::cout << myAccount.checkBalance() << '\n';	
	std::cout << yourAccount.checkBalance() << '\n';
	std::cout << accountPtr->checkBalance() << '\n';
	
	
	//delete the heap allocated object
	delete accountPtr;
	
	return(0);
}










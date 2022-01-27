#include <iostream>
#include "Account.h"


int main()
{
	//What is balance set to?
	Account myAccount(500);
	
	myAccount.deposit(1000);
	myAccount.withdraw(250);
	std::cout << myAccount.checkBalance() << '\n';


	
	return(0);
}




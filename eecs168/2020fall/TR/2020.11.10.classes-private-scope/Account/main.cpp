#include <iostream>
#include "Account.h"
#include <string>
int main()
{
	//What is the balance?
	Account myAccount;
	
	//myAccount is an instance of the 
	//Account class
	myAccount.deposit(100);
	myAccount.withdraw(40);
	
	std::cout << myAccount.checkBalance() << '\n';
		
	
	return(0);
}

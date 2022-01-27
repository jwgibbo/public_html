#include <iostream>
#include "Account.h"

//Goal: swap the balances in two Accounts
void moneySwap(Account& account1, Account& account2)
{
	//board work: define this
}

int main()
{
	//What is balance set to?
	Account myAccount(100);
	Account yourAccount;
	
	myAccount.transfer(yourAccount, myAccount.checkBalance() );
	
	std::cout << "myAccount balance: ";
	std::cout << myAccount.checkBalance() << '\n';
	
	std::cout << "yourAccount balance: ";
	std::cout << yourAccount.checkBalance() << '\n';

	
	return(0);
}




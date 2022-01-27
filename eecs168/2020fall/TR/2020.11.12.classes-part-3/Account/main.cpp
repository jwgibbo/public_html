//main.cpp
#include <iostream>
#include "Account.h"
#include <string>

//Define a function that swaps the amounts in
//two account
void moneySwap(Account& account1, Account& account2)
{
	double tempBalance = account1.checkBalance();
	
	account1.withdraw( account1.checkBalance() );
	account1.deposit( account2.checkBalance() );
	
	account2.withdraw( account2.checkBalance() );
	account2.deposit( tempBalance );
}

int main()
{
	//What is the balance?
	Account myAccount;
	Account yourAccount;
	
	myAccount.deposit(100);
	yourAccount.deposit(50);
	
	myAccount.transfer(yourAccount, 20);
	
	//transfer all your money to myAccount
	yourAccount.transfer(myAccount, yourAccount.checkBalance()); 
	
	moneySwap(myAccount, yourAccount);
	
	std::cout << "My Account balance: ";
	std::cout << myAccount.checkBalance() << '\n';
	
	std::cout << "Your Account balance: ";
	std::cout << yourAccount.checkBalance() << '\n';	
	
	return(0);
}










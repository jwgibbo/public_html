//Account.cpp
#include "Account.h"

Account::Account(double startingBalance)
{
	if(startingBalance > 0)
	{
		balance = startingBalance;
	}
	else
	{
		balance = 0;
	}
}

bool Account::deposit(double amount)
{
	if( amount > 0 )
	{	
		balance = balance + amount;
		return (true);
	}
	else
	{
		return (false);
	}	
}

bool Account::withdraw(double amount) 
{
	if( amount <= balance && amount > 0 )
	{
		balance = balance - amount;
		return (true);
	}
	else
	{
		return (false);
	}	
}

double Account::checkBalance() const
{
	//I shouldn't be changing the balance
	return(balance);
}

bool Account::transfer(Account& destination, double amount)
{
	if(amount > 0 && amount <= balance)
	{
		// destination.deposit(amount);
		
		//Accessing private member is allowed
		//because we're in the Account class
		destination.balance += amount;
		balance = balance - amount;
		return (true);
	}
	else
	{
		return (false);
	}
}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


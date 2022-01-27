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
	if(amount > 0)
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
	if(amount <= balance && amount > 0)
	{
		balance = balance - amount;
		return (true);
	}
	else
	{
		return(false);
	}
}

double Account::checkBalance() const
{	
	return(balance);
}


bool Account::transfer(Account& destination, double amount)
{
	if(amount > 0 && amount <= balance)
	{
		balance = balance - amount;
		// option: destination.deposit(amount)
		destination.balance += amount;
		return (true);
	}
	else
	{
		return (false);
	}
}
		














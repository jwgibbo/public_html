//Account.cpp
#include "Account.h"

Account::Account()
{
	//initialize all member variables
	balance = 0;
}

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

double Account::checkBalance()
{
	return(balance);
}



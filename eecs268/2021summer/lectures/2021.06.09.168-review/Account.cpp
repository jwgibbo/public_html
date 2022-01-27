//Account.cpp

#include "Account.h"

Account::Account(double initialBalance)
{
	if(initialBalance > 0)
	{
		m_balance = initialBalance;
	}
	else
	{
		m_balance = 0;
	}
}


bool Account::withdrawl(double amount)
{
	if(amount <= m_balance && amount > 0)
	{
		m_balance = m_balance - amount;
		return(true);
	}
	else
	{
		return(false);
	}
}
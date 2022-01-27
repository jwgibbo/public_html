//Account.h
#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account
{
	private:
	double m_balance;
	
	public:	
	Account(double initialBalance);
	bool withdrawl(double amount);
	
};


#endif
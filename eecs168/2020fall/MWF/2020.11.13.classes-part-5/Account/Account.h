//Account.h

#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account
{
	//public members are accessible
	//in any scope through an instance
	public:
	//Member methods
	Account();
	Account(double startingBalance);
	
	bool deposit(double amount);
	bool withdraw(double amount);
	double checkBalance() const;
	bool transfer(Account& destination, double amount);
	//Private members are only accessible
	//by this class' members
	private:
	double balance;
	
};


#endif
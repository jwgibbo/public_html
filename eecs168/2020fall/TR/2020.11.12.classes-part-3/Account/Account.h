//Account.h

#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account
{
	//member in the public scope are
	//accessible in any scope:
	//In this class definition
	//In other scope (e.g. main)
	//    through an instance
	public:
	Account();
	bool deposit(double amount);
	bool withdraw(double amount);
	double checkBalance() const;
	bool transfer(Account& destination, double amount);
	//Members in the private scope
	//are only accessible in the class
	//class defintion (e.g. by
	//class members)
	private:
	double balance;
};


#endif
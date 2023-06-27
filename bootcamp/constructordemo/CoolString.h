//CoolString.h
#ifndef COOLSTRING_H
#define COOLSTRING_H
#include <iostream>
class CoolString
{
	private:
	char* m_arr;
	int m_length;
	
	public:
	CoolString(int length);
	
	//Copy Constructor
	CoolString(const CoolString& orig);
	
	//Destructor
	~CoolString();
	
	//Move Constructor
	CoolString(CoolString&& move_target);
	
	//Store entry at the index
	//returns true if its successful
	//otherwise returns false
	bool setEntry(int index, char entry);
	
	//returns the character at the index
	//precondition: index is valid
	char getEntry(int index) const;
	
	//getter for the length
	int length() const;
};

#endif


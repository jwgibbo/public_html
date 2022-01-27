#ifndef COOL_STRING_H
#define COOL_STRING_H

#include <iostream>
class CoolString
{
	private:
	//NOTE: A convention I follow is the m_ 
	//prefix to a member variable name
	char* m_array;
	int m_size;
	
	public:
	//Constructor
	CoolString(int size);
	
	//Destructor
	//-Automatically called when the object is 
	//	deallocated (either from stack or heap)
	//-Name is always ~ClassName()
	//-Cannot take parameters
	//-Typically only defined if your class 
	//	allocates something on the heap
	//-No return type listed
	~CoolString();
	
	//BOARD WORKS
	int size() const; //returns the size of the array
	char getAt(int index) const; //return the character at an index
	bool setAt(int index, char entry); //stores character at an index
	
	//Passing by reference, but promising not to 
	//change the object passed in.
	bool isSameSize(const CoolString& otherCS) const;
	
};








#endif

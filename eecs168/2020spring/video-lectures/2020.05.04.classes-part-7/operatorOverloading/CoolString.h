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
	
	//Copy Constructor
	//-Called when...
	//  1) When an object is passed by value
	//  2) When passing an existing object of the same
	//     type to a constructor call (forced)
	//  GOAL: Makes a "deep copy" of the original
	CoolString(const CoolString& original);
	
	
	
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
	
	//Overload an operator
	bool operator==(const CoolString& rhs) const;
	bool operator!=(const CoolString& rhs) const;
};








#endif

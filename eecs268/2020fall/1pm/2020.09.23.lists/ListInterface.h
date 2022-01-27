//ListInterface.h

#ifndef LIST_INTERFACE_H
#define LIST_INTERFACE_H

template <typename T>
class ListInterface
{
	public:
	
	//We can insert at indices 1 to length + 1
	virtual void insert(int index, T entry) = 0;
	
	//Return the entry at an index if it exists
	//otherwise thrown an exception
	virtual T getEntry(int index) const = 0;

	//Returns length of the list
	virtual int length() const = 0;
	
	//Override the value at an index
	virtual void replace(int index, T entry) = 0;
	
	//Removes entry at index
	virtual void remove(int index) = 0;
};
#endif
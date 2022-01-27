#ifndef LIST_INTERFACE_H
#define LIST_INTERFACE_H

template <typename T>
class ListInterface
{
	//IMPORTANT NOTE: Our indexing start at 1
	
	//General note: 
	//Any method that takes an index can throw an 
	//exception if index is invalid

	/*
	public:	
	virtual T getEntry(int index) const = 0;
	
	//Place new entry at the specific index
	virtual void insert(T entry, int index) = 0;
	
	//Remove node at given index
	virtual void remove(int index) = 0;
	
	//Returns number of elements in list
	virtual int length() const = 0;
	*/
	//More methods to come
};

#endif
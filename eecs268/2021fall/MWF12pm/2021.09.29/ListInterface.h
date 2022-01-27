//ListInterface.h

#ifndef LIST_INTERFACE_H
#define LIST_INTERFACE_H

template <typename T>
class ListInterface
{
	public:
	virtual void insert(int index, T entry) = 0;
	virtual void remove(int index) = 0;
	virtual T getEntry(int index) const = 0;
	//More methods to come in the future...
	
};

#end
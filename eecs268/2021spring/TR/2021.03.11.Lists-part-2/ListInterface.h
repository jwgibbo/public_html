//ListInterface.h
#ifndef LIST_INTERFACE_H
#define LIST_INTERFACE_H

template <typename T>
class ListInterface
{
	public:
	virtual ~ListInterface() {}
	virtual int length() const = 0;
	virtual T getEntry(int index) const = 0;
	virtual void insert(int index, T entry) = 0;
	
};


#endif
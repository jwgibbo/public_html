#ifndef LIST_INTERFACE_H
#define LIST_INTERFACE_H

template <typename T>
class ListInterface
{
	public:
	//more methods coming...
	virtual ~ListInterface(){}
	
	
	virtual void insert(int index, T entry) = 0;
	virtual T getEntry(int index) const = 0;
	virtual void remove(int index) = 0;
	virtual void replace(int index, T entry) = 0;
	virtual int length() const = 0;
};

//No cpp included because interfaces only
//have a header file
#endif

#ifndef LIST_INTERFACE_H
#define LIST_INTERFACE_H

template <typename T>
class ListInterface
{
	public:
	virtual T getEntry(int index) const = 0;
	
	//More methods coming Wednesday
};


#endif
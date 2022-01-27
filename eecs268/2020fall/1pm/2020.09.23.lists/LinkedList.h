//LinkedList.h

#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include "Node.h"
#include "ListInterface.h"

template <typename T>
class LinkedList : public ListInterface<T>
{
	public:
	//We can insert at indices 1 to length + 1
	void insert(int index, T entry);
	
	//Return the entry at an index if it exists
	//otherwise thrown an exception
	T getEntry(int index) const ;

	//Returns length of the list
	int length() const;
	
	//Override the value at an index
	void replace(int index, T entry);
	
	//Removes entry at index
	void remove(int index);
	
	private:
	int m_length;
	Node<T>* m_front;
};
#endif
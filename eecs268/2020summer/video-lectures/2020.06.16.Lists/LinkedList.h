#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include "ListInterface.h"
#include "Node.h"

template <typename T>
class LinkedList : public ListInterface<T>
{
	private:
	Node<T>* m_front;
	int m_length;
	
	public:
	//Methods that will never be listed in the 
	//interface:
	LinkedList();
	
	//LinkedList(const LinkedList& orig);
	//void operator=(const LinkedList& rhs);
	
	/*
	//Methods that must be implemented because
	//of List interface:
	virtual T getEntry(int index) const;
	
	//Place new entry at the specific index
	virtual void insert(T entry, int index);
	
	//Remove node at given index
	virtual void remove(int index);
	
	//Returns number of elements in list
	virtual int length() const;
	*/
};
#include "LinkedList.cpp"
#endif
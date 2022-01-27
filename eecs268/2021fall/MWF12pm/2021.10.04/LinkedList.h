//LinkedList.h

#ifndef LINKED_LIST_H
#define LINKED_LIST_H
#include "ListInterface.h"
#inclue "Node.h"

template <typename T>
class LinkedList : public ListInterface<T>
{
	private:
	Node<T>* m_front;
	int m_length;
	
	public:
	LinkedList();
	virtual T getEntry(int index) const;
	
	virtual void insert(int index, T entry);
	virtual void remove(int index);
	//More methods to come in the future...
	virtual int getLength() const;
};

#end
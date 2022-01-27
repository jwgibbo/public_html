#include "StackOfInts.h"

StackOfInts::StackOfInts()
{
	m_top = nullptr;
}

void StackOfInts::push(int entry)
{
	//We can't use Stack allocated Nodes
	//Node myTempNode(entry);
	//myTempNode.setNext(m_top);
	//m_top = &myTempNode;
	
	Node* temp = new Node(entry);
	temp->setNext(m_top);
	m_top = temp;	
}
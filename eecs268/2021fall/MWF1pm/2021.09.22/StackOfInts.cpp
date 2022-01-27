
#include "StackOfInts.h"

StackOfInts::StackOfInts()
{
	m_top = nullptr;
}


void StackOfInts::push(int entry)
{
	Node* newTop = new Node(entry);
	newTop->setNext(m_top);
	m_top = newTop;	
}
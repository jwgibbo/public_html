#include "StackOfInts.h"

StackOfInts::StackOfInts()
{
	m_top = nullptr;
}


void StackOfInts::push(int entry)
{
	Node* newTop = new Node(entry);
	
	//if newTop is not null, then the node was created
	if(newTop != nullptr)
	{
		newTop->setNext(m_top);
		m_top = newTop;
	}
	//we ran out of memory
	else
	{
		throw(std::runtime_error("Out of memory! Help! How!? Close netflix"));
	}
}
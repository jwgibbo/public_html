//Node.cpp
#include "Node.h"


Node::Node(int entry)
{
	m_entry = entry;
	m_next = nullptr;
}	


int Node::getEntry() const
{
	return(m_entry);	
}

void Node::setEntry(int entry)
{
	m_entry = entry;
}

Node* Node::getNext() const
{
	return(m_next);
}

void Node::setNext(Node* next)
{
	m_next = next;
}
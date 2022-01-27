//Node.cpp

#include "Node.h"

Node::Node(int entry)
{
	//initialize the member variables
	m_next = nullptr;
	m_entry = entry;
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
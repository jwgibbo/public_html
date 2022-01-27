#ifndef NODE_H
#define NODE_H

class Node
{
	private:
	int m_entry;
	Node* m_next;
	
	public:
	Node(int entry);
	int getEntry() const;
	void setEntry(int entry);
	Node* getNext() const;
	void setNext(Node* next);
};

#endif
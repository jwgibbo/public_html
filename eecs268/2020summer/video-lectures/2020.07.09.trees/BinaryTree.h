
//Node based implemenation
//of a Binary Tree

//BNode is a Node with left and right
//pointers, getters/setters for left,
//right, and entry
#include "BNode.h"

template <typename T>
class BinaryTree
{
	private:
	BNode<T>* m_root;
	
	//recursive search
	bool search(T entry, BNode<T>* subtree);
	
	
	
	public:
	//sets m_root to nullptr
	BinaryTree();
	
	//We will not be implementing add
	void add(T entry);
	
	//return true if the entry is in the 
	//tree
	bool search(T entry);
};
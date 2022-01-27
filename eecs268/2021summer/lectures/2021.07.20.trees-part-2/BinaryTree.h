//BinaryTree.h

//Sketch of a Binary Tree class

//Assume we have a Binary Node class
//that contains get/set left and right
#include "BNode.h"

template <typename T>
class BinaryTree
{
	private:
	BNode<T>* m_root;
	
	int recCountNodes(BNode<T>* subtree) const;
	
	public:
	BinaryTree();
	void add(T entry);//Assume this works
	
	//Returns the count of nodes in the tree
	int countNodes() const;
	
};
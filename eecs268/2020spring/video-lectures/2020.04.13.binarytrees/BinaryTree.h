//We haven't made this yet
//But you should be able to make it on
//your own
#include "BinaryNode.h"

//Pretend implementation BinaryTree

template <typename T>
class BinaryTree
{
	private:
	BinaryNode<T>* m_root;
	bool search(T entry, BinaryNode<T>* subtree);
	
	public:
	BinaryTree();
	void add(T entry);//we won't implement
	
	//Return true is entry is in the tree
	bool search(T entry);
};

#include "BinaryTree.cpp"
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
	
	int countLeaves(???);
	int count(???);//recursive count that does all the work
	bool search(T entry, BinaryNode<T>* subtree);
	
	public:
	BinaryTree();
	void add(T entry);//we won't implement
	int count() const; //returns a count of how many
						//nodes are in the tree (0 or more)
	int countLeaves() const; //counts how many leaves are
						      //in the tree
	
	//Return true is entry is in the tree
	bool search(T entry);
};

#include "BinaryTree.cpp"
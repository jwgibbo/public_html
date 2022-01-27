

//Binary Nodes have left and right pointers
//with getLeft and getRight methods
#include "BNode.h"

template <typename T>
class BinaryTree
{
	private:
	BNode<T>* m_root;
	bool recSearch(T target, BNode<T>* subtree);
	
	public:
	BinaryTree();//sets m_root to nullptr
	void add(T entry);//assume this works
	
	bool search(T target) const;
	
};
//BinaryTree.h

//Assume BNodes have left and right pointers
// 		and an entry, with getters/setters
//		for each of those
#include "BNode.h"

template <typename T>
class BinaryTree
{
	private:
	BNode<T>* m_root;
	bool recSearch(T target, BNode<T>* subtree) const;
	
	public:
	BinaryTree();//Sets m_root to nullptr
	void add(T entry);//assume this works
	bool search(T target) const;
};
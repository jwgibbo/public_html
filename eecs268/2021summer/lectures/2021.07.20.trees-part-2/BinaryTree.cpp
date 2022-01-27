//Binary.cpp

template <typename T>
int BinaryTree<T>::countNodes() const
{
	//return the result of the private
	//recursive method. We just tell that
	//method where to start
	return(recCountNodes(m_root));
}

//Private recursive function 
template <typename T>
int BinaryTree<T>::recCountNodes(BNode<T>* subtree) const
{
	if(subtree == nullptr)
	{
		return(0);
	}
	else
	{
		int leftSubtreeCount= recCountNodes(subtree->getLeft());
		int rightSubtreeCount = recCountNodes(subtree->getRight());
		return(1+leftSubtreeCount+rightSubtreeCount);
	}		
}
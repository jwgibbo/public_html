//BinaryTree.cpp


template <typename T>
bool BinaryTree<T>::search(T target) const
{
	return(recSearch(target, m_root));	
}

template <typename T>
bool BinaryTree<T>::recSearch(T target, BNode<T>* subtree)
{
	if(subtree == nullptr)
	{
		return (false);
	}
	else if( subtree->getEntry() == target )
	{
		return (true);
	}
	else
	{
		//We pointing a node, but we don't have a match
		//Search the left subtree
		bool isInLST = recSearch(target, subtree->getLeft());
		
		//Search the right subtree
		bool isInRST = recSearch(target, subtree->getRight());
		
		return( isInLST || isInRST );
	}
	
}
//BinaryTree.cpp

//public facing search
template <typename T>
bool BinaryTree<T>::search(T target) const
{
	return(recSearch(target, m_root));
}

//private recursive search
template <typename T>
bool BinaryTree<T>::recSearch(T target, BNode<T>* subtree) const
{
	if(subtree == nullptr)
	{
		//empty subtree
		return(false);
	}
	else if(subtree->getEntry() == target)
	{
		return(true);
	}
	else
	{
		//search both the subtrees!
		bool isInLST = recSearch(target, subtree->getLeft());
		bool isInRST = recSearch(target, subtree->getRight());
		return( isInLST || isInRST );
	}
}

//public search
template <typename T>
bool BinaryTree<T>::search(T entry)
{
	return(search(entry, m_root));
}

//public count
template <typename T>
bool BinaryTree<T>::search(T entry)
{
	return(count(???));
}

//private search
template <typename T>
bool BinaryTree<T>::search(T entry, BinaryNode<T>* subtree)
{
	//base cases
	//1) if subtree is nullptr then the subtree we're 
	//    searching is empty. Return false
	//2) if we've found it, return true
	//NOTE always check for nullptr first!
	if(subtree == nullptr)
	{
		return(false);
	}
	else if(subtree->getEntry() == entry)
	{
		return(true);
	}
	else
	{
		//search lst and rst
		bool isInLST = search(entry, subtree->getLeft());
		bool isInRST = search(entry, subtree->getRight());
		return( isInLST || isInRST );
	}
}
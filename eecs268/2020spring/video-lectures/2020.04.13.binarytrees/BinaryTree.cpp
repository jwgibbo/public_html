
//public search
template <typename T>
bool BinaryTree<T>::search(T entry)
{
	return(search(entry, m_root));
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
		//BOARD WORK
		//search the left subtree and the right subtree
		//what will the recursive call(s?) look like
		//and how will we return their result?
	}
}

//public search
template <typename T>
bool BinaryTree<T>::search(T entry)
{
	return( search(entry, m_root) );
}

//private search
template <typename T>
bool BinaryTree<T>::search(T entry, BNode<T>* subtree)
{
	//if the subtree is empty
	if(subtree == nullptr)
	{
		return(false);
	}
	//Board work! Finish the definition
}


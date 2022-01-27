

template <typename T>
LinkedList<T>::LinkedList()
{
	m_front = nullptr;
	m_length = 0;
}

template <typename T>
int LinkedList<T>::length() const
{
	return(m_length);
}
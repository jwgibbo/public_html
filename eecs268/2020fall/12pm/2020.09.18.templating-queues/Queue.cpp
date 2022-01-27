//Queue.cpp

template <typename T>
Queue<T>::Queue()
{
	m_front = nullptr;
	m_back = nullptr;
}

template <typename T>
void Queue<T>::enqueue(T entry)
{
	Node<T>* temp = new Node<T>(entry);
	
	//finish defining
	//NOTE: what happens when queue is empty?
	
}
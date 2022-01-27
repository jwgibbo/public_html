

template <typename T>
Queue<T>::Queue()
{
	m_front = nullptr;
	m_back = nullptr;
}

template <typename T>
Queue<T>::Queue(const Queue<T>& orig)
{
	Node<T>* jumper = orig.m_front;
	
	//front and back of the Queue
	//we're constructing
	m_front = nullptr;
	m_back = nullptr;
	
	while( jumper != nullptr )
	{
		enqueue(jumper->getEntry());
		jumper = jumper->getNext();
	}
}

template <typename T>
void Queue<T>::operator=(const Queue<T>& rhs)
{
	//Make sure we don't cause a memory
	//leak!
	while( !isEmpty() )
	{
		dequeue();
	}
	
	//Make a deep copy of the rhs
	Node<T>* jumper = rhs.m_front;
	while( jumper != nullptr )
	{
		enqueue(jumper->getEntry());
		jumper = jumper->getNext();
	}	
}
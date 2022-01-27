//Queue.cpp


//Define the copy constructor
template <typename T>
Queue<T>::Queue(const Queue<T>& orig)
{
	Node<T>* jumper = orig.m_front;
	
	//Recall, we're in a constructor
	m_front = nullptr;
	m_back = nullptr;
	
	while( jumper != nullptr )
	{
		//look at each value
		//put it in the "copy" 
		enqueue(jumper->getEntry());
		
		//move jumper to the next node
		jumper = jumper->getNext();
	}	
}
template <typename T>
void Queue<T>::operator=(const Queue<T>& rhs)
{
	//Empty out the queue
	
	//deep copy of rhs
	
}
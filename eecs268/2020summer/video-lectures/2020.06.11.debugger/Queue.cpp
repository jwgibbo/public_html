
template <typename T>
Queue<T>::Queue()
{
	m_front = nullptr;
	m_back = nullptr;
}

template <typename T>
void Queue<T>::enqueue(T entry)
{
	//what if we're adding to an empty Queue?
	if(isEmpty())
	{
		//this entry is at the front and
		//the back of the queue. Deal
		//with both pointers
		m_back = new Node<T>(entry);
		m_front = m_back;
	}
	else
	{
		//just update what's at the back
		Node<T>* temp = m_back;
		m_back = new Node<T>(entry);
		temp->setNext(m_back);
	}
}

template <typename T>
bool Queue<T>::isEmpty() const
{
	return(m_front==nullptr);
}
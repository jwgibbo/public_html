
template <typename T>
Stack<T>::Stack()
{
	m_top = nullptr;
}

template <typename T>
Stack<T>::push(T entry)
{
	//empty stack
	if(m_top == nullptr)
	{
		m_top = new Node<T>(entry);
	}
	//non-empty stack
	else
	{
		//Get another pointer to point
		//at the top node
		Node<T>* temp = m_top;
		
		//Use top to point a new node with
		//the new entry
		m_top = new Node<T>(entry);
		
		//connect the new top to the old top
		m_top->setNext(temp);
	}
}
//Stack.cpp

template <typename T>
Stack<T>::Stack()
{
	m_top = nullptr;
}

template <typename T>
T Stack<T>::peek() const
{
	if(!isEmpty())
	{
		return(m_top->getEntry());
	}
	else
	{
		//what do we return
		throw(std::runtime_error("Peek called on empty stack"));
	}
}
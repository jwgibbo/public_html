#include "Stack.h"

template <typename T>
Stack<T>::Stack()
{
	m_top = nullptr;
}

template <typename T>
T Stack<T>::peek() const
{
	if( !isEmpty() )
	{
		return( m_top->getEntry() );	
	}
	else
	{
		//returning isn't an option
		throw( std::runtime_error("Peek called on empty stack") );
	}
}
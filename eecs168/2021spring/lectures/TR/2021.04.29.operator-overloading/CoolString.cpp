//CoolString.cpp

#include "CoolString.h"


CoolString::CoolString(int size)
{
	//create the char array
	m_arr = new char[size];
	//store the size
	m_size = size;
}

CoolString::~CoolString()
{
	delete[] m_arr;
}

int CoolString::getSize() const
{
	return(m_size);
}

bool CoolString::setEntry(int index, char symbol)
{
	if(0 <= index && index < m_size)
	{
		m_arr[index] = symbol;
		return(true);
	}
	else
	{
		return(false);
	}
}

char CoolString::getEntry(int index) const
{
	if(0 <= index && index < m_size)
	{
		return(m_arr[index]);
	}
	else
	{
		//We don't have a great option
		//for a return value
		return('\0');
		//Stay tuned for Exceptions in 268
	}
}


bool CoolString::operator==(CoolString rhs)
{
	if(m_size == rhs.m_size)
	{
		for(int i=0; i<m_size; i++)
		{
			if(m_arr[i] != rhs.m_arr[i])
			{
				return(false);
			}
		}
		return(true);
	}
	else
	{
		return(false);
	}
	
}














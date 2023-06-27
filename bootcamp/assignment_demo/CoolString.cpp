//CoolString.cpp

#include "CoolString.h"

//Precondition: valid length
CoolString::CoolString(int length)
{
	std::cout << "Standard constructor called!" << std::endl;
	m_length = length;
	m_arr = new char[m_length];
	
	//initialize array to all '?'
	for(int i=0; i<m_length; i++)
	{
		m_arr[i] = '?';
	}
}

//Define copy constructor
CoolString::CoolString(const CoolString& orig)
{
	std::cout << "Copy constructor called for CoolString of length ";
	std::cout << orig.m_length << std::endl;
	m_arr = new char[orig.m_length];
	m_length = orig.m_length;
	
	//copy each element
	for(int i=0; i<m_length; i++)
	{
		m_arr[i] = orig.m_arr[i];
	}
}

CoolString::CoolString(CoolString&& move_target)
{
	std::cout << "Move constructor moving CoolString of length ";
	std::cout << move_target.m_length << std::endl;
	//transfer the target's resources to this object
	this->m_arr = move_target.m_arr;
	this->m_length = move_target.m_length;
	
	//Set the target's member to a default state
	move_target.m_arr = nullptr;
	move_target.m_length = 0;
}


CoolString::~CoolString()
{
	std::cout << "Destructor called for Cool String of length ";
	std::cout << m_length << std::endl;
	delete[] m_arr;
}

CoolString& CoolString::operator=(const CoolString& rhs)
{
	std::cout << "copy assignment called" << std::endl;
	//Make sure to free up anything the left hand side
	if (m_arr != nullptr)
	{
		delete[] m_arr;
	}
	
	m_arr = new char[rhs.m_length];
	m_length = rhs.m_length;
	
	//copy each element
	for(int i=0; i<m_length; i++)
	{
		m_arr[i] = rhs.m_arr[i];
	}
	
	return *this;
}

CoolString& CoolString::operator=(CoolString&& rhs)
{
	std::cout << "move assignment called" << std::endl;
	//Make sure the object isn't being assigned to itself
	//Otherwise, do nothing
	if (this != &rhs)
	{
		std::cout << "proceeding with move" << std::endl;
		this->m_arr = rhs.m_arr;
		this->m_length = rhs.m_length;
		
		//Set the target's member to a default state
		rhs.m_arr = nullptr;
		rhs.m_length = 0;
	}
	else
	{
		std::cout << "move aborted; object assigned to itself" << std::endl;
	}
	
	return *this;
}

bool CoolString::setEntry(int index, char entry)
{
	if( index >= 0 && index < m_length )
	{
		m_arr[index] = entry;
		return(true);
	}
	else
	{
		return(false);
	}
}
	
char CoolString::getEntry(int index) const
{
	return( m_arr[index] );
}

int CoolString::length() const
{
	return(m_length);
}







#include "CoolString.h"

CoolString::CoolString(int size)
{
	//create an array of the given size
	//assumes size to be valid

	//Just for lecture, don't do this normally:
	std::cout << "Constructor called!\n";
	
	//store the size
	m_size = size;
	
	//create an array of the given size
	m_array = new char[m_size];
	
	//initialize the array
	for(int i=0; i<m_size;  i++)
	{
		m_array[i] = '\0';//null character
	}
}

CoolString::~CoolString()
{
	//Just for lecture, don't do this normally:
	std::cout << "Destructor called!\n";
	
	//Goal: delete everything this object put
	//on the heap
	delete[] m_array;
}
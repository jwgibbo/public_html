

#include "SomeClass.h"

SomeClass::SomeClass(int data)
{
	m_data = data;
}

void SomeClass::interactWithData(void func(int)) const
{
	func(m_data);
}
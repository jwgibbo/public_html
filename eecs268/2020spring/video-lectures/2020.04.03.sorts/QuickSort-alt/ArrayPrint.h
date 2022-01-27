
#ifndef ARRAY_PRINT_H
#define ARRAY_PRINT_H

template <typename T>
class ArrayPrint
{
	public:
	void print(T arr[], int size);

	/**
	*	@post prints all elements in arr from first to last, inclusively. (first, last)
	*/
	void printRange(T arr[], int first, int last);
};

#include "ArrayPrint.hpp"

#endif 

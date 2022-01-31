/**
*	@file : QuickSort.h
*	@author :  John Gibbons
*	@date : 2014.03.26
*/

#ifndef QUICK_SORT_H
#define QUICK_SORT_H

#include "ArrayPrint.h"

template<typename T>
class QuickSort
{
	public:

	/**
	*	@pre arr is a vaild array of T of size elements
	*	@post arr will be sorted in ascending order using the last element as the pivot
	*/
	void sort(T arr[], int size);


	/**
	*	@pre arr is a vaild array of T of size elements
	*	@post arr will be sorted in ascending order using the median pivot
	*/	
	void sortWithMedian(T arr[], int size);

	private:
	/**
	*	@pre arr is a vaild array of T of size elements
	*	@post arr will be sorted in ascending order
	*/
	void quickSort(T arr[], int first, int last, bool median);
	
	/**
	*	@pre arr is a vaild array of T of size elements, first is < last and both are 
	*		valid indices of arr.
	*	@post The pivot value with be in the correct index. All elements with indicies 
	*		less than the pivot's index are less than or equal to the pivot.
	*		All elements with indicies greater than the pivot's index are
	*		 greater than or equal to the pivot.  
	*
	*	@return The index of the pivot after partitioning	
	*/	
	int partition(T arr[], int first, int last, bool median);

	/**
	*	@pre arr is a vaild array of T of size elements
	*	@post the median pivot value of first, last, and mid is in the last index of the array
	*/
	void setMedianPivot(T arr[], int first, int last);

	ArrayPrint<T> ap;
};

#include "QuickSort.hpp"

#endif

/**
*	@file : QuickSort.hpp
*	@author :  John Gibbons
*	@date : 2014.03.26
*/

template<typename T>
void QuickSort<T>::sort(T arr[], int size)
{
	quickSort(arr, 0, size-1, false);
}

template<typename T>
void QuickSort<T>::sortWithMedian(T arr[], int size)
{
	quickSort(arr, 0, size-1, true);
}

template<typename T>
void QuickSort<T>::quickSort(T arr[], int first, int last, bool median)
{
	int pivotIndex = 0;

	if(first < last)
	{
		pivotIndex = partition(arr, first, last, median);
		
		//ap.printRange(arr, first, pivotIndex-1);
		quickSort(arr, first, pivotIndex-1, median);

		//ap.printRange(arr, pivotIndex+1, last);
		quickSort(arr, pivotIndex+1, last, median);
	}
}

template<typename T>
int QuickSort<T>::partition(T arr[], int first, int last, bool median)
{
	int curLeft = first;
	int curRight = last-1;//put the pivot in the last position
	
	if(median)
	{
		setMedianPivot(arr, first, last);
	}

	int pivotIndex = last;
	T pivot = arr[pivotIndex];
	T temp;

	while(curLeft < curRight)
	{
		while(arr[curLeft] <= pivot && curLeft<curRight)
		{
			curLeft++;
		}

		while(arr[curRight] > pivot && curLeft<curRight)
		{
			curRight--;
		}
		//std::cout << "Swapping " << arr[curLeft] << " and " << arr[curRight] << std::endl;	
		temp = arr[curLeft];
		arr[curLeft] = arr[curRight];
		arr[curRight] = temp;
	}

	
	
	//put the pivot in its final position and return that index
	if( arr[pivotIndex] < arr[curRight] )
	{
		temp = arr[pivotIndex];
		arr[pivotIndex] = arr[curRight];
		arr[curRight] = temp;
		pivotIndex = curRight;
	}

	//std::cout << "Partitioning with pivot = : " << pivot << std::endl;
	//ap.printRange(arr, first, last);

	return(pivotIndex);
}

template <typename T>
void QuickSort<T>::setMedianPivot(T arr[], int first, int last)
{
	/* Find the median of three values in list, use it as the pivot */
	int mid = (first + last)/2;
	T temp;

	//if first is greater than mid swap them
	if (arr[first] > arr[mid])
	{
		temp = arr[first];
		arr[first] = arr[mid];
		arr[mid] = temp;
	}

	//if first is greater than last swap them
	if (arr[first] > arr[last])
	{
		temp = arr[first];
		arr[first] = arr[last];
		arr[last] = temp;
	}

	//if mid is greater than last swap them
	if (arr[mid] > arr[last])
	{	
		temp = arr[mid];
		arr[mid] = arr[last];
		arr[last] = temp;
	}

	//swap mid with first to put the pivot in the first 
	temp = arr[mid];
	arr[mid] = arr[last];
	arr[last] = temp;
} 


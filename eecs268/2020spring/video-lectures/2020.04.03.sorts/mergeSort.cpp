//helper function to merge presorted sub arrays
template<typename T>
void merge(T a1[], T a2[], int size1, int size2)
{
	T* merged = new T[(size1+size2)];
	int a1Index=0;
	int a2Index=0;
	int mergedIndex=0;
	
	while(a1Index < size1 && a2Index < size2)
	{
		if( a1[a1Index] < a2[a2Index] )
		{
			merged[mergedIndex] = a1[a1Index];
			a1Index++;
		}
		else
		{
			merged[mergedIndex] = a2[a2Index];
			a2Index++;
		}
		
		mergedIndex++;
	}
	
	if(a1Index < size1)
	{
		for(int i=a1Index; i<size1; i++)
		{
			merged[mergedIndex] = a1[i];
			mergedIndex++;
		}
	}
	
	if(a2Index < size2)
	{
		for(int i=a2Index; i<size2; i++)
		{
			merged[mergedIndex] = a2[i];
			mergedIndex++;
		}
	}

	for(int i=0; i<(size1+size2); i++)
	{
		a1[i] = merged[i];
	}
	
	delete[] merged;		
}

//mergesort, breaks the original array into sub arrays 
//and then merges adjacent elements in sorted order,
//evenutally merges into the final array
template<typename T>
void mergeSort(T arr[], int size)
{
	int mid = size/2;
	int leftSize = mid;
	int rightSize = size-leftSize;
	T* left = arr;
	T* right = (arr+mid);
	
	if(size <= 1)
	{
		//Array already sorted
		return;
	}
	else
	{
		mergeSort(left,leftSize);
		mergeSort(right, rightSize);		
		merge(left, right, leftSize, rightSize);
	}
}

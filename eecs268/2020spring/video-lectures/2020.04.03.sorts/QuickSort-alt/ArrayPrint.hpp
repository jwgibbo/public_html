

//utility for printing arrays 
template <typename T> 
void ArrayPrint<T>::print(T arr[], int size) 
{
	std::cout << "[";
	for(int i=0; i<size; i++)
	{
		std::cout << arr[i];
		
		if(i<size-1)
		{
			std::cout << ", "; 
		}
	}
	std::cout << "]" << std::endl;
} 

template <typename T> 
void ArrayPrint<T>::printRange(T arr[], int first, int last) 
{
	std::cout << "[";
	for(int i=first; i<=last; i++)
	{
		std::cout << arr[i];
		
		if(i<last)
		{
			std::cout << ", "; 
		}
	}
	std::cout << "]" << std::endl;
} 

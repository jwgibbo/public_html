//Sketching of an array based implementation of a 
//Min heap
#include <stdexcept>

template <typename T>
class HeapAsArray : public HeapInterface<T>
{
	private:
	T* m_arr;
	int m_arrSize;
	int m_heapSize;
	
	void resize(); //doubles array size when called
					//copies all old elements
	
	//Board Work: Write a recursive definition for upheap
	void upheap(int index);//upheaps value at given index	
	
	//Board Work: Write a recursive definition for downheap
	void downheap(int index);
	
	public:
	void add(T entry);
	
	//Board Work: implement public remove
	void remove(); //throws exception if empty
	
};

#include "HeapAsArray.cpp"
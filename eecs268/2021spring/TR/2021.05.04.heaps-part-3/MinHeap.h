//MinHeap.h


template <typename T>
class MinHeap
{
	private:
	T* m_arr;
	int m_arraySize;
	int m_heapSize;
	void resize();//assume it works
					//makes more room in array
	void upheap(int index);
	void downheap(int index);
	
	public:
	MinHeap();
	void add(T entry);
	void remove();
	
};
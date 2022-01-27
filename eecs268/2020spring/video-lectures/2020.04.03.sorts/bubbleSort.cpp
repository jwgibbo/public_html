#include <cstdlib>
using namespace std;

//swaps adjacent elements a pair at a time
template <typename T>
void bubbleSort(T a[], int n)
{
  bool sorted = false;
  T tmp;
  int i, j;
  for (i=0; i < n-1 && !sorted; i++)
    {
      sorted = true;
      for (j=0; j < n-1-i; j++)
	  if (a[j+1] < a[j]) //compare adjacent elements
	  { //swap a[j] and a[j+1]
	    tmp = a[j];
	    a[j] = a[j+1];
	    a[j+1] = tmp;
	    sorted = false;
	  }
    }
}  // end bubbleSort


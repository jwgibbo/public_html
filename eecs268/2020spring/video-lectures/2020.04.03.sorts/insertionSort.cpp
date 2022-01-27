//insertionsort takes elements one at a time and inserts them into their correct posistion in the array.

template <typename T>
void insertionSort(T a[], int n)
{  
  int i, j;
  for (i = 1;i < n; i++)
    { 
      T nextItem = a[i];
      for (j = i-1;  j >= 0 && a[j] > nextItem; j--)
	a[j+1] = a[j];
      a[j+1] = nextItem;
    }  
}  



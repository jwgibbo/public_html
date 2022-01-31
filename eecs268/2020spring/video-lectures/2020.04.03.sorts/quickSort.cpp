#include <cstdlib>
using namespace std;

//quicksort first chooses an array element as a pivot then partitions the rest of the array by moving elements smaller elements before the pivot and greater elements after it.

template <typename T>
void setPivot(T a[], int first, int last)
{
  /* Find the median of three values in list, use it as the pivot */
  int mid = (first + last)/2;
  
  //if first is greater than mid swap them
  if (a[first] > a[mid])
    swap (a[first],a[mid]);
  //if first is greater than last swap them
  if (a[first] > a[last])
    swap (a[first],a[last]);
  //if mid is greater than last swap them
  if (a[mid] > a[last])
    swap (a[mid],a[last]);
  //swap mid with first to put the pivot in the first pos
  swap (a[mid],a[first]);
}

template <typename T>
void q_sort(T a[], int left, int right, bool median)
{
  T pivot, l_hold, r_hold;
  
  l_hold = left;
  r_hold = right;
  if(median == true)
    setPivot(a,left,right);
  pivot = a[left];
  while (left < right)
    {
      while ((a[right] >= pivot) && (left < right))
	right--;
      if (left != right)
	{
	  a[left] = a[right];
	  left++;
	}
      while ((a[left] <= pivot) && (left < right))
	left++;
      if (left != right)
	{
	  a[right] = a[left];
	  right--;
	}
    }
  a[left] = pivot;
  pivot = left;
  left = l_hold;
  right = r_hold;
  if (left < pivot)
    q_sort(a, left, pivot-1, median);
  if (right > pivot)
    q_sort(a, pivot+1, right, median);
}
//quicksort with pivot = first element
template <typename T>
void quickSort(T a[], int n)
{
  q_sort(a, 0, n - 1,false);
}

//quicksort with median of three pivot
template <typename T>
void quickSort3(T a[], int n)
{
  q_sort(a,0,n - 1,true);
}



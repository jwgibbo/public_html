#include <cstdlib>
using namespace std;

template <typename T>
int indexOfLargest(const T a[], int size)
// ---------------------------------------------------
// Finds the largest item in an array.
// Precondition: a is an array of size items, size >= 1.
// Postcondition: Returns the index of the largest 
// item in the array. The arguments are unchanged.
// ---------------------------------------------------
{
   int indexSoFar = 0;  // index of largest item found so far
   for (int currentIndex = 1; currentIndex < size; ++currentIndex) 
   {  // Invariant: a[indexSoFar] >= a[0..currentIndex-1]
     if (a[currentIndex] > a[indexSoFar])
         indexSoFar = currentIndex;
   }  // end for

   return indexSoFar;  // index of largest item
}  // end indexOfLargest

template <typename T>
void selectionSort(T a[], int n)
// ---------------------------------------------------
// Sorts the items in an array into ascending order.
// Precondition: a is an array of n items.
// Postcondition: The array a is sorted into ascending order; n is unchanged
// Calls: indexOfLargest, swap.
// ---------------------------------------------------
{
   // last = index of the last item in the subarray of items yet to be sorted
   // largest = index of the largest item found

   for (int last = n-1; last >= 1; --last)
   {  // Invariant: a[last+1..n-1] is sorted and > a[0..last]

      // select largest item in a[0..last]
      int largest = indexOfLargest<T>(a, last+1);

      // swap largest item a[largest] with a[last]
      swap<T>(a[largest], a[last]);
   } // end for
}  // end selectionSort


//Original code from:
//     https://en.cppreference.com/w/cpp/container/vector/insert
//Modified by Prof. John Gibbons
//2023.06.26
#include <iostream>
#include <iterator>
#include <vector>
 
void vec_print(int example_num, const std::vector<int>& container)
{
    std::cout << example_num << ". ";
    for (const int num: container)
        std::cout << num << ' ';
    std::cout << std::endl;
}
 
int main ()
{
    std::vector<int> c1;//empty vector

    //put 3 100s in a vector
    c1.push_back(101);
    c1.push_back(102);
    c1.push_back(103);
	vec_print(1, c1);

    std::vector<int>::iterator it = c1.begin();
    it = c1.insert(it, 200); //inserts at the beginning 
    vec_print(2, c1);
 
    c1.insert(it, 2, 300);
    vec_print(3, c1);

    // it no longer valid, get a new one:
    it = c1.begin(); //returns an iterator to beginning of c1
 
    std::vector<int> c2(2, 400);//put 2 400s in the vector

    //add all of c2's content to c1
	//the it+2 means start at the location of it
	//then move 2 to the right
	//NOTE: You can also say c1.begin()+2 instead of it+2
    c1.insert(it+2, c2.begin(), c2.end());
    vec_print(4, c1);


	//Create two arrays and add all their contents to c1
    int arr[] = {501, 502, 503};
    const int ARR_SIZE = 3;
    c1.insert(c1.begin(), arr, arr + ARR_SIZE);
    vec_print(5, c1);

	//this is adding a newly created, anonymous array
    c1.insert(c1.end(), {601, 602, 603});
    vec_print(6, c1);
}

#include <iostream>

//Assume the array is filled
//only with parens
bool parenChecker(char arr[], int size)
{
	Stack<char> leftParens;
	//Our definition below

	for(int i=0; i<size; i++)_
	{
		if(arr[i] == '(')
		{
			leftParens.push('(');
		}
		else if(arr[i] == ')')
		{
			if(leftParens.isEmpty())
			{
				return false;
			}
			else
			{
				leftParens.pop();
			}
		}
	}
	
	if(leftParens.isEmpty())
	{
		return true;
	}
	else
	{
		return false;
	}
}

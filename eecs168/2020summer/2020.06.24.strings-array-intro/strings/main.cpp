#include <iostream>
#include <string>

int main()
{	
	std::string email="";
	std::string domain=".edu";
	
	email = "jwgibbo";
	
	email = email + '@';//string + char
	
	email = email + "gmail";//string + constant character array
	
	email = email + domain;//string + string
	
	std::cout << "My email is: " << email << '\n';
	
	//compare string to "something"
	if(email == "jwgibbo@gmail.edu")
	{
		std::cout << "Hey that's my gmail account!\n";
	}
	
	//string.at(index) == char
	if(email.at(0) == 'j')
	{
		std::cout << "That's a little J!\n";
	}
	
	return(0);
}
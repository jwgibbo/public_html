prog: main.o Account.o
	g++ -std=c++11 -g -Wall main.o Account.o -o prog
	
main.o: main.cpp Account.h
	g++ -std=c++11 -g -Wall -c main.cpp

Account.o: Account.h Account.cpp
	g++ -std=c++11 -g -Wall -c Account.cpp
	
clean:
	rm *.o prog
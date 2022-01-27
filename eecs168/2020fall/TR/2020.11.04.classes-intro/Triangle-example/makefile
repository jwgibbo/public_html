prog: main.o Triangle.o
	g++ -std=c++11 -g -Wall main.o Triangle.o -o prog
	
main.o: main.cpp Triangle.h
	g++ -std=c++11 -g -Wall -c main.cpp

Triangle.o: Triangle.h Triangle.cpp
	g++ -std=c++11 -g -Wall -c Triangle.cpp
	
clean:
	rm *.o prog
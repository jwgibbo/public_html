prog: main.o Course.o
	g++ -std=c++11 -g -Wall main.o Course.o -o prog
	
main.o: main.cpp Course.h
	g++ -std=c++11 -g -Wall -c main.cpp

Course.o: Course.h Course.cpp
	g++ -std=c++11 -g -Wall -c Course.cpp
	
clean:
	rm *.o prog
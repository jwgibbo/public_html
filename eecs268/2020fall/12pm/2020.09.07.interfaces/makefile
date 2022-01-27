prog: main.o Circle.o  
	g++ -std=c++11 -Wall -g main.o Circle.o -o prog

main.o: main.cpp Shape.h
	g++ -std=c++11 -Wall -g -c main.cpp

Circle.o: Circle.h Circle.cpp
	g++ -std=c++11 -Wall -g -c Circle.cpp
	
clean:
	rm *.o prog
prog: main.o Circle.o Triangle.o
	g++ -std=c++11 -Wall -g Circle.o  Triangle.o main.o -o prog

main.o: main.cpp Shape.h
	g++ -std=c++11 -Wall -g -c main.cpp

Circle.o: Circle.h Circle.cpp
	g++ -std=c++11 -Wall -g -c Circle.cpp

Triangle.o: Triangle.h Triangle.cpp
	g++ -std=c++11 -Wall -g -c Triangle.cpp

clean:
	rm *.o prog
prog: main.o SomeClass.o AnotherClass.o
	g++ -std=c++11 -g -Wall main.o SomeClass.o AnotherClass.o -o prog
	
main.o: main.cpp
	g++ -std=c++11 -g -Wall -c main.cpp

SomeClass.o: SomeClass.h SomeClass.cpp
	g++ -std=c++11 -g -Wall -c SomeClass.cpp

AnotherClass.o: AnotherClass.h AnotherClass.cpp
	g++ -std=c++11 -g -Wall -c AnotherClass.cpp

clean:
	rm *.o prog
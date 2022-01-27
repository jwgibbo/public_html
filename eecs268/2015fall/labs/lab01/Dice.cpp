/**
*	@file : Dice.cpp
*	@author :  John Gibbons
*	@date : 2014.01.29
*	Purpose: Implementation of Dice Class
*/

#include "Dice.h"

Dice::Dice() 
{ 
	m_numSides = 6;
	/** initialize random seed: */
	srand (time(NULL));//Old C style NULL
}


Dice::Dice(int numSides)
{
	m_numSides = numSides;
	/** initialize random seed: */
	srand (time(NULL));//Old C style NULL
}


int Dice::getNumSides()
{
	return(m_numSides);
}

int Dice::roll()
{
	
	/** Get back a pseudo-random number */
	return(rand()%m_numSides + 1);
}

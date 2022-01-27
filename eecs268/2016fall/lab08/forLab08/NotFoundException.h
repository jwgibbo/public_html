//  Created by Frank M. Carrano and Tim Henry.
//  Copyright (c) 2013 __Pearson Education__. All rights reserved.

/** @file NotFoundException.h */

#ifndef _NOT_FOUND_EXCEPTION
#define _NOT_FOUND_EXCEPTION

#include <stdexcept>
#include <string>

using namespace std;

class NotFoundException : public logic_error
{
public:
   NotFoundException(const string& message = "");
}; // end NotFoundException 
#endif

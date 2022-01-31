//  Created by Frank M. Carrano and Tim Henry.
//  Copyright (c) 2013 __Pearson Education__. All rights reserved.

/** @file NotFoundException.cpp */
#include "NotFoundException.h"  

NotFoundException::NotFoundException(const string& message)
         : logic_error("Precondition Violated Exception: " + message)
{
}  // end constructor

// End of implementation file.


//  Created by Frank M. Carrano and Tim Henry.
//  Copyright (c) 2013 __Pearson Education__. All rights reserved.

/** A class of nodes for a link-based binary tree.
 Listing 16-2.
 @file BinaryNode.h */
 
#ifndef _BINARY_NODE
#define _BINARY_NODE

template<typename NodeItemType>
class BinaryNode
{   
private:
   NodeItemType              item;           // Data portion
   BinaryNode<NodeItemType>* leftChildPtr;   // Pointer to left child
   BinaryNode<NodeItemType>* rightChildPtr;  // Pointer to right child

public:
   BinaryNode();
   BinaryNode(const NodeItemType& anItem);
   BinaryNode(const NodeItemType& anItem,
              BinaryNode<NodeItemType>* leftPtr,
              BinaryNode<NodeItemType>* rightPtr);

   void setItem(const NodeItemType& anItem);
   NodeItemType getItem() const;
   
   bool isLeaf() const;

   BinaryNode<NodeItemType>* getLeftChildPtr() const;
   BinaryNode<NodeItemType>* getRightChildPtr() const;
   
   void setLeftChildPtr(BinaryNode<NodeItemType>* leftPtr);
   void setRightChildPtr(BinaryNode<NodeItemType>* rightPtr);            
}; // end BinaryNode

#include "BinaryNode.cpp"

#endif 

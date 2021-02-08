# Pairing-heaps
Pairing heaps is a simplified and modern form of Fibonacci heaps. It also contain the property of min heap or heap data structure with self adjusting structure so that it rearranges themselves to remain balanced  They are modification of binomial heap.  Pairing is basically known for fast running time operations. 
node has a pointer pointing towards the left child and left child point towards A pairing heap would either a empty heap or a tree consisting of root element . 
All parents nodes have smaller value than their child nodes value
Each the other or next sibling of child. 
Basic operations :-
Join / merge in pairing heaps
If  merge operation occurs between a  non-empty and a empty heap ,then merge function would just return that non-empty heap
And if both heaps are non-empty , then it would return a heap where the root of merged heap would be the smallest root of the two heaps .
Find minimum :-
Finding minimum element is very simple and easy . We just have to get the top element of the heap.
Find minimum function would return the minimum element of the heap 
Insertion :-
Insert function will insert an element in the existing pairing heap. Merge operation will be used for insertion .
Inserting an element similar to merging the elements in the heap or merging two heaps , one of them have single element 
Deletion:-
Deletion in Pairing Heap only happens at root node. First delete links between root, left child and all the siblings of the left child.
Then Merge tree subtrees that are obtained by detaching the left child and all siblings by the two pass method and delete the root node.
Merge the detached subtrees from left to right in one pass and then merge the subtrees from right to left to form the new heap without violation of conditions of min-heap. This process takes O(log n) time where n is the number of nodes.

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:55:25 2021

@author: Hassan
"""
# create a class of pairing heap
class Pairingheap:
# initilize the constructor
    def __init__(self):
# create an heap that starts with zero
        self.heap = [0]
# set as size as 0
        self.size = 0
# create a root variable and assign min heap
        x = min(self.heap)
        self.root = x
        
# create an insert function thats takes as parameter  
    def Insert_value(self, value):
# Append the value in heap
        self.heap.append(value)
# apppend the size
        self.size = self.size + 1

# create a merge function thats takes 2 parameter root1 and root 2
    def Merge(self, R1, R2):
# Appplying the condition
        if R1 == None:
            return R2
        elif R2 == None:
            return R1
        elif R1 < R2:
            self.heap.append(R2)
            return R1
# If condition fails then apply the else block
        else:
            self.heap.append(R1)
        return R2
    
# create a function delete
    def Delete(self):
# set heap as None
        if self.heap == None:
# rise an exception
            raise Exception ("List index out of range")
        else:
# runs else block
            self.root = None
# with heap index 1
            x = self.heap[1]
# swap the variables x and y
            self.heap[1] = self.heap[-1]
            y = self.heap[-1]
            abc = self.heap.pop(-1)
            self.size = self.size - 1
            return abc

# create a Function minmum
    def Minimum(self):
# applied condition when root is none
        if self.root==None:
            print("Pairing Heap is empty")
        else:
            return self.root

# create a function size
    def Size(self):
        print (len(self.heap))

#Driver Code
heap = Pairingheap()

# Calling the functions and insering their values
print("Pairing heap upon Insertion:")
heap.Insert_value(1)
heap.Insert_value(10)
heap.Insert_value(15)
heap.Insert_value(2)
heap.Insert_value(6)
heap.Insert_value(9)
print(heap.heap)
print()

print("---------------------------------------------")

print("The minimum value in pairing heap is:")
print(heap.Minimum())
print()

print("---------------------------------------------")

print("Pairing heaps after merging the roots are:")
print("Smaller root =",heap.Merge(10,2))
print("Heap after merge is:")
print(heap.heap)
print()

print("---------------------------------------------")

print("The Pairing Heap after deleting is:")
heap.Delete()
heap.Delete()
print(heap.heap)
print()

print("---------------------------------------------")

print("The size of Pairing Heap is:")
heap.Size()
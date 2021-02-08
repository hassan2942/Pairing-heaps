# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:17:05 2021

@author: Hassan
"""
# create a class of pairing heap
class PairingHeap:
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
    def Insert_Root(self, value):
# Append the value in heap
        self.heap.append(value)
# apppend the size
        self.size = self.size + 1

# create a merge function thats takes 2 parameter root1 and root 2
    def MRAR(self, R1, R2):
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
    def Delete_Root(self):
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
            dlt = self.heap.pop(-1)
            self.size = self.size - 1
            return dlt

# create a Function minmum
    def FD(self):
# applied condition when root is none
        if self.root==None:
            print("Pairing Heap is empty")
        else:
            return self.root

# create a functoin size
    def Size(self):
        print (len(self.heap))

#Driver Code
heap = PairingHeap()
 
print("Pairing Heap upon Insertion:")
heap.Insert_Root(1)
heap.Insert_Root(13)
heap.Insert_Root(14)
heap.Insert_Root(10)
heap.Insert_Root(35)
heap.Insert_Root(86)
print(heap.heap)
print()
 
print("Getting Mininmum in pairing heap:")
print(heap.FD())
print()
 
print("Merging roots in pairing heaps:")
print("Smaller root =",heap.MRAR(10,2))
print("Heap after merge:")
print(heap.heap)
print()
 
print("Pairing Heap after deleting:")
heap.Delete_Root()
heap.Delete_Root()
print(heap.heap)
print()
 
print("Size of Pairing Heap:")
heap.Size()
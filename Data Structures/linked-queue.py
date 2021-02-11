#! /bin/python3

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.last = None

    def enQueue(self, val): 
        if self.last is None: 
            self.head =Node(val) 
            self.last =self.head 
            self.display()
        else: 
            self.last.next = Node(val) 
            self.last.next.prev = self.last 
            self.last = self.last.next
            self.display()
    
    def deQueue(self): 
        if self.head is None: 
            print('Operation failed. Queue is empty')
        else: 
            iNode= self.head.val
            self.head = self.head.next
            return iNode 

    def peek(self):
        if self.isEmpty():
            print('Queue is empty, Nothing to peek')
        else: 
            return self.head.val 
   
    def size(self): 
        iNode=self.head 
        count=0
        while iNode is not None: 
            count += 1
            iNode=iNode.next
        return count 
            
    def isEmpty(self): 
        if self.head is None: 
            return True
        else: 
            return False
               
    def display(self):
        if self.isEmpty():
            print('Queue is empty.')
        else: 
            iNode = self.head 
            while iNode is not None: 
                print(f'{iNode.val} => ', end=' ') 
                iNode = iNode.next
            print(f'\nSize of queue: {self.size()}')

if __name__ == '__main__':
    newQueue = LinkedQueue()
    inputs = [5,4,3,2,1]
    #Checking the empty condition
    newQueue.display()
    for i in inputs:
        newQueue.enQueue(i)
    #deQueueing 2 elements
    for i in range(3):
        print(f'deQueued out {newQueue.deQueue()} from the queue')
    #Displaying the queue after deQueueing out
    newQueue.display()
    #Trying to deQueue out an extra element to check the empty condition
    for i in range(2):
        val = newQueue.deQueue()
        if val != -1:
            print(f'deQueued out {val} from the queue')
    newQueue.display()
    #Trying to deQueue from an empty queue
    newQueue.deQueue()
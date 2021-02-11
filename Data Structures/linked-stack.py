#! /bin/python3

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def push(self, val):
        if self.isEmpty():
            self.head = Node(val)
            self.display()
        else:
            nextNode = Node(val)
            nextNode.next = self.head
            self.head = nextNode
            self.display()

    def pop(self):
        if self.isEmpty():
            print('Cannot pop. Stack is empty') 
            return -1  
        else:
            top_node = self.head
            self.head = self.head.next
            top_node.next = None
            return top_node.val
     
    def peek(self): 
        if self.isEmpty():
            return None
        return self.head.val

    def display(self):
        iNode = self.head
        if self.isEmpty():
            print("No elements in the stack :)")
         
        else:
            count = 0
            while(iNode != None):  
                print(f'{iNode.val} =>', end=' ') 
                count += 1
                iNode = iNode.next
            print(f'\nNo. of elements: {count}')
            return
   
if __name__ == '__main__':
    newStack = LinkedStack()
    #Checking the initial state of the stack
    newStack.display()
    inputs = [5,4,3,2,1]
    for i in inputs:
        newStack.push(i)
    #Popping 3 elements
    for i in range(3):
        print(f'Popped out {newStack.pop()} from the stack')
    #Displaying the stack after popping out
    newStack.display()
    #Trying to pop out an extra element to check the empty condition
    for i in range(3):
        val = newStack.pop()
        if val != -1:
            print(f'Popped out {val} from the stack')










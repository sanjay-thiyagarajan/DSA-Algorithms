#! /bin/python3

class BinaryTree:
    def __init__(self, size):
        self.size = size
        self.tree = [None] * size  
    
    def root(self, key):
        if self.tree[0] != None:
            print('Root already exists!')
        else:
            self.tree[0] = key
    
    def left(self, key, parent):
        if self.tree[parent] == None:
            print(f'Failed to add child at {(parent*2)+1}.\n R: Parent not found')
        else:
            self.tree[(parent*2)+1] = key
  
    def right(self, key, parent):
        if self.tree[parent] == None:
            print(f'Failed to add child at {(parent*2)+2}. \n R: Parent not found')
        else:
            self.tree[(parent*2)+2] = key
 
    def display(self):
        print('[', end='')
        for i in range(self.size):
            if self.tree[i] != None:
                print(self.tree[i], end=",")
            else:
                print("-", end=",")
        print(']')
 
if __name__ == '__main__':
    btree = BinaryTree(10)
    btree.root('A')
    btree.right('C', 0)
    btree.left('D', 1)
    btree.right('E', 1)
    btree.right('F', 2)
    btree.display()
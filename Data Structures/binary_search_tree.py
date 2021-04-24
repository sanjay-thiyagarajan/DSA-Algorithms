#! /bin/python3
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
    
#Inserting function
def insert(parent, value):
  if parent is None:
    return Node(value)
  else:
    if parent.value == value:
      return parent
    elif parent.value < value:
      parent.right = insert(parent.right, value)
    else:
      parent.left = insert(parent.left, value)
  return parent
    
#Printing in in_ordered order
def in_order(parent):
    if parent:
        in_order(parent.left)
        print(parent.value)
        in_order(parent.right)

def post_order(parent):
    if parent:
        post_order(parent.left)
        post_order(parent.right)
        print(parent.value)

def pre_order(parent):
    if parent:
        print(parent.value)
        pre_order(parent.left)
        pre_order(parent.right)

if __name__ == '__main__':
    root = int(input('Enter the value of root node: '))
    tree = Node(root)
    vals = []
    vals = list(map(int, input('Enter the values to be placed in the tree: ').split(' ')))
    for v in vals:
        tree = insert(tree, v)
    print('Printing in-order\n')
    in_order(tree)
    print('Printing pre-order\n')
    pre_order(tree)
    print('Printing post-order\n')
    post_order(tree)
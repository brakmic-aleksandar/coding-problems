""" Challenge

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left' """

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root, s = ''):
    """ Tarverses binary tree recursively (from left to right) and serializes it into CSV format, complexity O(n)"""
    #whole point of this is to avoid last comma in serialized string, 
    #if its true and we get to return statement it means whole function and its subsequent calls are done 
    isEntry = s == '' 

    if root is None:
        s += 'null,'
    else:
        s += root.val + ','
        s = serialize(root.left, s)
        s = serialize(root.right, s)
    return s if not isEntry else s[:-1]

def deserialize(s):
    """ Tarverses CSV string and generates binary tree, complexity O(n)"""

    def add(node, l):
        """ Recursively generates binary tree"""
        #if list is empty we are done, there are no more items to deserialize
        if l.count == 0:  
            return
        # this part of code will continually keep adding left nodes until it gets to null node
        # once it gets to null node it means there are no more left nodes to add, 
        # afterwards it will try to create right node(if there its value it's not null, offcourse), and restart process of
        # left node generation again, node values are contained in list whose items are removed when deserialized.
        v = l.pop(0)
        if v != 'null':
            node.left = Node(v)
            add(node.left, l)
        v = l.pop(0)
        if v != 'null':
            node.right = Node(v)
            add(node.right, l)

    l = s.split(",")
    root = Node(l.pop(0))
    add(root, l)
    return root


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left' 


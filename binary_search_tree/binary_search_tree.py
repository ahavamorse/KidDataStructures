"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If value is smaller and belongs on the left
        if value < self.value:
            # If already has a left child
            if self.left:  # *Recursive Case/Step*
                # Pass value to child to insert
                self.left.insert(value)
            # Else doesn't have a left child
            else:   # *Base Case*
                # Insert a node with the value on the left
                self.left = BSTNode(value)
        # If value is larger and belongs on the right
        elif value >= self.value:
            # If already has a right child
            if self.right:  # *Recursive Case/Step*
                # Pass value to child to insert
                self.right.insert(value)
            # Else doesn't have a right child
            else:   # *Base Case*
                # Insert a node with the value on the right
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If value is target
        if target == self.value:
            return True
        # If target is less it would be on the left
        elif target < self.value:
            # If has a left child
            if self.left:
                # Passes target to left child to check
                return self.left.contains(target)
            # Else doesn't have a left child
            else:
                # Value doesn't exist
                return False
        # If target is more it would be on the right
        elif target > self.value:
            # If has right child
            if self.right:
                # Passes target to right child to check
                return self.right.contains(target)
            # Else doesn't have a right child
            else:
                # Value doesn't exist
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # If has right child
        if self.right:
            # Ask child to find max
            return self.right.get_max()
        # Else is max
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call function on self
        self.value = fn(self.value)
        # Check for left child
        if self.left:
            # Ask left child to call function
            self.left.for_each(fn)
        # Check for right child
        if self.right:
            # Ask right child to call function
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()
        # if no left child, print self, then print right subtree

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass
        # Create a queue to keep track of nodes
        # Add the first node to the queue
        # While the queue is not empty
            # remove the first node from the queue
            # print the removed node
            # add the node's children to the queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        print(self.value)
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass  # root, left, right

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass  # left, right, root

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()

import unittest
import random
import sys
import io

class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BSTNode(5)

    def test_insert(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(6)
        self.assertEqual(self.bst.left.right.value, 3)
        self.assertEqual(self.bst.right.left.value, 6)

    def test_handle_dupe_insert(self):
        self.bst2 = BSTNode(1)
        self.bst2.insert(1)
        self.assertEqual(self.bst2.right.value, 1)

    def test_print_traversals(self):
        # WARNING:  Tests are for Print()
        # Debug calls to Print() in functions will cause failure

        stdout_ = sys.stdout  # Keep previous value
        sys.stdout = io.StringIO()

        self.bst = BSTNode(1)
        self.bst.insert(8)
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(6)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(2)

        self.bst.in_order_print()

        output = sys.stdout.getvalue()
        self.assertEqual(output, "1\n2\n3\n4\n5\n6\n7\n8\n")
        '''
        sys.stdout = io.StringIO()
        self.bst.bft_print()
        output = sys.stdout.getvalue()
        self.assertTrue(output == "1\n8\n5\n3\n7\n2\n4\n6\n" or
                        output == "1\n8\n5\n7\n3\n6\n4\n2\n")
        '''
        sys.stdout = io.StringIO()
        self.bst.dft_print()
        output = sys.stdout.getvalue()
        self.assertTrue(output == "1\n8\n5\n7\n6\n3\n4\n2\n" or
                        output == "1\n8\n5\n3\n2\n4\n7\n6\n")

    '''
        sys.stdout = io.StringIO()
        self.bst.pre_order_dft()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "1\n8\n5\n3\n2\n4\n7\n6\n")

        sys.stdout = io.StringIO()
        self.bst.post_order_dft()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "2\n4\n3\n6\n7\n5\n8\n1\n")

        sys.stdout = stdout_  # Restore stdout
'''


if __name__ == '__main__':
    unittest.main()
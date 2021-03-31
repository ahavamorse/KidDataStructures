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
        queue = []
        # Add the first node to the queue
        queue.append(self)
        # While the queue is not empty
        while queue:
            # Remove the first node from the queue
            current_node = queue[0]
            queue.pop(0)
            # Print the removed node
            print(current_node.value)
            # Add the node's children to the end of the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        print(self.value)
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()
        # Could also use a stack here:
        # Create a stack and add the first node
        # While the stack is not empty
            # Remove the first node from the top of the stack
            # Print the removed node
            # Add the node's children to the top of the stack
            # Order matters and will be reversed in order

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # root, left, right
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # left, right, root
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

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

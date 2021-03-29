"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   When pushing in a Stack, arrays must insert values at index = 0 and shift the other values
   while linked lists insert it as the new head that points to the old head. When popping
   arrays remove the value from the beginning and shift the values, while linked lists simply
   replace the head with the next value.
"""
import doubly_linked_list.doubly_linked_list

class Stack:
    def __init__(self):
        self.size = 0

        """ # Array
        self.storage = []
        """
        # Linked List
        self.storage = doubly_linked_list.DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        """ # Array
        if self.size == 0:
            self.storage = [value]
        else:
            self.storage.insert(0, value)
        self.size += 1
        """
        # Linked List
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        """ # Array
        if self.size == 0:
            return None
        value = self.storage[0]     # Could just use pop(0) method of the array for these two lines
        self.storage.remove(value)  # pop(0) removes the first element and returns the value
        self.size -= 1              # Could also treat the end of the array as the top and append to
        return value                # and remove elements from the end (not faster because needs a new array)
        """
        # Linked List
        if self.size == 0:      # Take advantage of the size variable we have here
            return None
        self.size -= 1
        return self.storage.remove_from_head()

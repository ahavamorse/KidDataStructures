"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   When enqueueing with arrays simply appending the value is enough; with linked lists
   the value needs to be added to the tail and the pointers taken care of. When dequeueing
   with arrays the value and index 0 is removed and the other elements shifted; linked lists
   remove the head and take care of the pointers.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import doubly_linked_list.doubly_linked_list


class Queue:
    def __init__(self):
        self.size = 0
        """ # Array
        self.storage = []
        """
        # Linked List
        self.storage = doubly_linked_list.DoublyLinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        """ # Array
        if self.size == 0:
            self.storage = [value]
        else:
            self.storage.append(value)
        self.size += 1
        """
        # Linked List
        self.storage.add_to_tail(value)     # With a doubly linked list we can add to head or tail
        self.size += 1                      # but with a singly linked list we must add to tail

    def dequeue(self):
        """ # Array
        if self.size == 0:
            return None
        value = self.storage[0]
        self.storage.remove(value) # Could use pop(0) here
        self.size -= 1
        return value
        """
        # Linked List
        if self.size == 0:
            return None
        self.size -= 1                              # With a doubly linked list we can remove from head or tail
        return self.storage.remove_from_head()      # but with a singly linked list we must remove from head

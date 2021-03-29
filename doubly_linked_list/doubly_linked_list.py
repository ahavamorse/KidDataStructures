"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
''' # This was done in class
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    # Added code they started with
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print(self):
        curr_node = self.head
        print(curr_node)
        while curr_node.next is not None:
            curr_node = curr_node.next
            print(curr_node)
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        # Check if this is an empty list
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        # Check if this is an empty list
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
        elif node == self.tail:
            self.tail = node.prev
        self.length -= 1
        node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # Attempted on my own
        max = self.head.value
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value > max:
                max = current_node.value
        return max


# Singly Linked List Implementation on my own
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str___(self):
        return str(self.value)


class LinkedList:
    def __init__(self, node=node):
        self.head = node
        self.tail = node
        self.size = 1 if not Node else 0

    def __len__(self):
        return self.size

    def add_to_head(self, value):
        self.size += 1
        new_node = ListNode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, value):
        self.size += 1
        new_node = ListNode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_head(self, node):
        self.size -= 1
        old_head = self.head
        self.head = self.head.next
        return old_head
'''

# Doubly Linked List Implemented on my own
class ListNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.size = 1 if node is not None else 0
    
    def __len__(self):
        return self.size
    
    def add_to_head(self, value):
        self.size += 1
        new_node = ListNode(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def add_to_tail(self, value):
        self.size += 1
        new_node = ListNode(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
    
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
    
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)
    
    def delete(self, node):
        if not self.head and not self.tail: # Empty List
            return

        self.size -= 1
        if node == self.head and node == self.tail: # Only node in list
            self.head = None
            self.tail = None
        elif node == self.head: # Node is head
            self.head = node.next
        elif node == self.tail: # Node is tail
            self.tail = node.prev
        else:                   # Node is none of the above
            node.prev.next = node.next
            node.next.prev = node.prev
    
    def get_max(self):
        max = self.head.value
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            if current_node.value > max:
                max = current_node.value
        return max

import unittest

class DoublyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.node = ListNode(1)
        self.dll = DoublyLinkedList(self.node)

    def test_list_remove_from_tail(self):
        self.dll.remove_from_tail()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(33)
        self.assertEqual(self.dll.head.value, 33)
        self.assertEqual(self.dll.tail.value, 33)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_tail(), 33)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(68)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_tail(), 68)
        self.assertEqual(len(self.dll), 0)

    def test_list_remove_from_head(self):
        self.dll.remove_from_head()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_head(2)
        self.assertEqual(self.dll.head.value, 2)
        self.assertEqual(self.dll.tail.value, 2)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_head(), 2)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_head(55)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_head(), 55)
        self.assertEqual(len(self.dll), 0)

    def test_list_add_to_tail(self):
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(len(self.dll), 1)

        self.dll.add_to_tail(30)
        self.assertEqual(self.dll.tail.prev.value, 1)
        self.assertEqual(self.dll.tail.value, 30)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_tail(20)
        self.assertEqual(self.dll.tail.prev.value, 30)
        self.assertEqual(self.dll.tail.value, 20)
        self.assertEqual(len(self.dll), 3)

    def test_list_add_to_head(self):
        self.assertEqual(self.dll.head.value, 1)

        self.dll.add_to_head(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.head.next.value, 1)
        self.assertEqual(len(self.dll), 2)

    def test_list_move_to_end(self):
        self.dll.add_to_head(40)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.head.value, 40)

        self.dll.move_to_end(self.dll.head)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.prev.value, 1)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_tail(4)
        self.dll.move_to_end(self.dll.head.next)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.prev.value, 4)
        self.assertEqual(len(self.dll), 3)

    def test_list_move_to_front(self):
        self.dll.add_to_tail(3)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 3)

        self.dll.move_to_front(self.dll.tail)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.next.value, 1)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_head(29)
        self.dll.move_to_front(self.dll.head.next)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.next.value, 29)
        self.assertEqual(len(self.dll), 3)

    def test_list_delete(self):
        self.dll.delete(self.node)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(1)
        self.dll.add_to_head(9)
        self.dll.add_to_tail(6)

        self.dll.delete(self.dll.head.next)
        self.assertEqual(self.dll.head.value, 9)
        self.assertEqual(self.dll.head.next, self.dll.tail)
        self.assertEqual(self.dll.tail.value, 6)

        self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.value, 6)
        self.assertEqual(self.dll.tail.value, 6)
        self.assertEqual(len(self.dll), 1)

        self.dll.delete(self.dll.head)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

    def test_get_max(self):
        self.assertEqual(self.dll.get_max(), 1)
        self.dll.add_to_tail(100)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(55)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(101)
        self.assertEqual(self.dll.get_max(), 101)


if __name__ == '__main__':
    unittest.main()

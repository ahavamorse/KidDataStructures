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

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


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
        
        if not self.head and not self.tail:  # Empty List
            self.head = new_node
            self.tail = new_node
        else:   # List contains at least one element
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def add_to_tail(self, value):
        self.size += 1
        new_node = ListNode(value)
        
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_from_head(self):
        # Check for empty list
        if not self.head:
            return None

        head_value = self.head.value
        self.delete(self.head)
        return head_value
    
    def remove_from_tail(self):
        # Check for empty list
        if not self.head:
            return None

        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value
    
    def move_to_front(self, node):
        # This saves time if already at the front
        if node == self.head:
            return

        self.delete(node)
        self.add_to_head(node.value)
    
    def move_to_end(self, node):
        # This saves time if already at the end
        if node == self.tail:
            return

        self.delete(node)
        self.add_to_tail(node.value)
    
    def delete(self, node):
        if not self.head and not self.tail:  # Empty List
            return

        self.size -= 1
        if node == self.head and node == self.tail:  # Only one node in list
            self.head = None
            self.tail = None

        elif node == self.head:  # Node is only head
            self.head = node.next
            # Added this to keep the head from still pointing back at 'deleted' node
            self.head.prev = None
            # Added this to remove the pointers of the node being deleted
            node.delete()

        elif node == self.tail:  # Node is only tail
            self.tail = node.prev
            # Added this to keep the head from still pointing to 'deleted' node
            self.tail.next = None
            # Added this to remove the pointers of the node being deleted
            node.delete()

        else:
            # Node is none of the above (Also should check that the node is in the list
            node.prev.next = node.next
            node.next.prev = node.prev
            # Added this to remove the pointers of the node being deleted
            node.delete()
    
    def get_max(self):
        # Check for empty List
        if not self.head:
            return None

        max_value = self.head.value
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value

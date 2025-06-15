# linkedlist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

    def delete_nth_node(self, n):
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")
        if n <= 0:
            raise IndexError("Index must be a positive integer.")
        
        if n == 1:
            self.head = self.head.next
            return

        curr = self.head
        for i in range(n - 2):
            if not curr.next:
                raise IndexError("Index out of range.")
            curr = curr.next

        if not curr.next:
            raise IndexError("Index out of range.")
        
        curr.next = curr.next.next

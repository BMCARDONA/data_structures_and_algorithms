# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:    
            self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    # Note: Here, our node could ALREADY be in our linked list, OR 
    # its .prev and .null properties could both be pointing to null
    def insertBefore(self, node, nodeToInsert):
        # If we're dealing with linked list with one node, there's
        # nothing to do... 
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        # if node is head
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        # If we're dealing with linked list with one node, there's
        # nothing to do... 
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        # if node is tail
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
        
    # O(P) time | O(1) space, where p is the position
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            # Temporary variable
            nodeToRemove = node
            # Why can't next line come at end of while loop?
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    # O(1) time | O(1) space
    def removeNodeBindings(self, node):
        # Here, we're just redirecting the pointers of the node's
        # neighbors and of the node itself. 
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        # if node is not None, linked list DOES contain node with value
        return node is not None
            

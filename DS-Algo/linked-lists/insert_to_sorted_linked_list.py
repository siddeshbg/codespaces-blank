"""
Given a sorted linked list and a value to insert, 
write a function to insert the value in a sorted way.

Initial Linked List: 2->5->7->10->15
After inserting 9: 2->5->7->9->10->15

Algorithm
1) If Linked list is empty then make the node as
   head and return it.
2) If the value of the node to be inserted is smaller 
   than the value of the head node, then insert the node 
at the start and make it head.
3) In a loop, find the appropriate node after 
   which the input node (let 9) is to be inserted. 
   To find the appropriate node start from the head, 
   keep moving until you reach a node GN (10 in
   the below diagram) who's value is greater than 
   the input node. The node just before GN is the
appropriate node (7).
4) Insert the node (9) after the appropriate node
   (7) found in step 3.

"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, value):
        print("Appending: %s" % value)
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
    
    def insert(self, value):
        new_node = Node(value)
        # If Linked list is empty then make the node as head and return it
        if self.head is None:
            self.head = new_node
            return
        
        # If the value of the node to be inserted is smaller 
        # than the value of the head node, then insert the node 
        # at the start and make it head
        current_node = self.head
        if current_node.value > value:
            self.head = new_node
            new_node.next = current_node
        else:
            while current_node.value < value:
                previous_node = current_node
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    # last node
                    current_node.next = new_node
                    return   
            previous_node.next = new_node
            new_node.next = current_node

    
    def display_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    list1 = LinkedList()
    # list1.insert(-5)
    # list1.display_list()
    list1.append(2)
    list1.append(5)
    list1.append(7)
    list1.append(10)
    list1.append(15)
    print("Initial list")
    list1.display_list()

    print("Inserting 1")
    list1.insert(1)
    list1.display_list()

    print("Inserting 9")
    list1.insert(9)
    list1.display_list()

    print("Inserting 17")
    list1.insert(17)
    list1.display_list()
    
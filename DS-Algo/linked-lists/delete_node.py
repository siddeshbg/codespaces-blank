"""
Given a Singly Linked List, write a function to delete a given node.

Solution:
- when the node to be deleted is the first node, copy the data of 
the next node to the head and delete the next node. 
- when a deleted node is not the head node can be handled normally 
by finding the previous node and changing the next of the previous node. 
"""
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def delete_list(self, value):
        # If it is first node
        if self.head.data == value:
            self.head = self.head.next
        else:
            current_node = self.head
            next_node = current_node.next
            while next_node is not None:
                if next_node.data == value:
                    current_node.next = next_node.next
                next_node = next_node.next
                current_node = current_node.next
            
    
    def diplay_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()



if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(4)
    list1.append(7)
    list1.append(9)
    list1.append(12)
    print("Initial list")
    list1.diplay_list()
    print("deleted first node 4")
    # list1.delete_list(4)
    list1.delete_list(12)
    list1.diplay_list()

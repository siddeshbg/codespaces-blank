class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
    
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            previous = self.head
            self.head = Node(value)
            self.head.next = previous 
    
    def length(self):
        len = 0
        current = self.head
        while current is not None:
            len += 1
            current = current.next            
        return len
    
    def get_element(self, position):
        i = 0
        current = self.head

        while current is not None:
            if i == position:
                return current.value
            current = current.next
            i += 1
        return None
    


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append(5)
    list1.append(7)
    list1.append(9)
    list1.show_elements()
    print("Length of linked list = %s" % list1.length())
    print("Element at position 1: %s" % list1.get_element(1))

    list1.prepend(3)
    list1.show_elements()
class Node:
    data: str
    next: 'Node'

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    head:Node   

    def __init__(self,head):
        self.head=head

    def print_structure(self):
        current_node=self.head

        while (current_node is not None):
            print(current_node.data)
            current_node= current_node.next
            



first_node = Node('hola mundo')
second_node = Node('hola mundo2')
third_node = Node('hola mundo3')
first_node.next = second_node
second_node.next = third_node
structure = LinkedList(first_node)

structure.print_structure()
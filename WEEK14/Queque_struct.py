class Node:
    data: str
    next: 'Node'

    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    head:Node   

    def __init__(self,head):
        self.head=head

    def print_structure(self):
        current_node=self.head

        while (current_node is not None):
            print(current_node.data)
            current_node= current_node.next

    def queue(self, node):
        current_node=self.head

        while (current_node.next is not None):
            current_node= current_node.next

        current_node.next = node
            
    def dequeue(self, ):
        if self.head:
         self.head = self.head.next



first_node = Node('hola mundo')
second_node = Node('hola mundo2')
third_node = Node('hola mundo3')
first_node.next = second_node
second_node.next = third_node

structure = Queue(first_node)

fourth_node = Node('hola mundo4')
third_node.next = fourth_node

structure.print_structure()
structure.dequeue()
# print('----------')
# structure.print_structure()
# structure.dequeue()
# print('----------')
# structure.print_structure()
# structure.dequeue()
# print('----------')
# structure.print_structure()
# structure.dequeue()
# print('----------')
# structure.print_structure()
# structure.queue()
# print('----------')
# structure.print_structure()
# structure.queue()
# print('----------')
# structure.print_structure()
# structure.queue()
# print('----------')
# structure.print_structure()
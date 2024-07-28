class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def bubble_sort(self):
        end = None
        while end != self.head:
            swapped = False
            current = self.head
            while current.next != end:
                next_node = current.next
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = next_node
            end = current
            if not swapped:
                break

# Ejemplo de uso
linked_list = LinkedList()
linked_list.append(4)
linked_list.append(2)
linked_list.append(5)
linked_list.append(1)
linked_list.append(3)

print("Lista antes de ordenar:")
linked_list.print_list()

linked_list.bubble_sort()

print("Lista después de ordenar:")
linked_list.print_list()

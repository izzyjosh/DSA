from typing import Any
import ctypes

# singly linked list is a Data Structure that stores data that are linked together and each data has a locatiom that is placed in an entirely different place unlike list that stores data in location next to each other
# defining a class for each node
# A node is a class with two property (data to store and the address for the next node)


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


# Creating the linkedlist class
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert(self, new_node: Node) -> None:
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            last_node: Node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = new_node
            self.size += 1

    def printlist(self) -> None:
        if self.head is None:
            print("The list is empty")
        else:
            arr = []
            head = self.head
            while head is not None:
                arr.append(head.data)
                head = head.next
                print(head.data)
            print(arr)

    # function that print the size of the list
    def list_size(self) -> int:
        head = self.head
        size: int = 0
        while True:
            if head is None:
                break
            else:
                size += 1
                head = head.next
        else:
            return size
        return size

    def search(self, data: Any) -> bool:
        head = self.head
        while True:
            if head is None:
                break
            else:
                if head.data == data:
                    return True
                head = head.next
        return False

    def get_index(self, index: int) -> Any:
        head = self.head
        for i in range(index):
            if i == index:
                break
            head = head.next
            if head is None:
                return "index out of range"
        return head

    def insert_at(self, index: int, val) -> Any:
        newnode = Node(val)
        head = self.head
        prev = self.head
        if index == 0:
            prev = self.head
            self.head = newnode
            newnode.next = prev
            self.size += 1

        else:
            for i in range(index):
                if i == index:
                    break
                elif i == index - 1:
                    prev = head
                head = head.next
                if head is None:
                    return "index out of range"
            # After the loop head is containing the index i want to insert to
            # prev is containing the node before the node i want to insert to
            prev.next = newnode
            newnode.next = head
            self.size += 1

    def empty_list(self) -> Any:
        if self.head:
            self.head = None
        else:
            return "list is empty"

    def delete_val(self, val: Any) -> None:
        len_list = self.list_size()

        if self.head.data == val:
            self.head = self.head.next
            self.size -= 1
            return

        head = self.head
        prev = self.head
        for i in range(len_list):
            if head.next.next is None and head.next.data == val:
                prev = head
                prev.next = None
                break

            if head.next.data == val:
                prev = head
            elif head.data == val:
                break
            head = head.next

        prev.next = head.next
        self.size -= 1

    #def partition(self, k: int) -> None:
#        for i in range(self.list_size()):
#            for j in range(self.list_size() - 1):
#                # get the current obj using the get_index method
#                curr = self.get_index(j)
#                curr_obj = ctypes.cast(id(curr), ctypes.py_object).value

#                next = self.get_index(j + 1)
#                next_obj = ctypes.cast(id(next), ctypes.py_object).value
#                # swap when the current value is greater than k and the next value is less than k
#                if curr_obj.data >= k and next_obj.data <= k:
#                    n = curr_obj.data
#                    curr_obj.data = next_obj.data
#                    next_obj.data = n

    def reverse(self) -> None:
        head = self.head
        for i in range(self.list_size() // 2):
            last = self.get_index(self.list_size() - 1 - i)
            new_last = ctypes.cast(id(last), ctypes.py_object).value
            n = head.data
            head.data = new_last.data
            new_last.data = n

            head = head.next

    def n_node(self, n) -> None:
        if n > self.size or n < 1:
            print("index out of range")
        else:
            index = self.size - n
            head = self.head
            for i in range(index):
                head = head.next
            print(head.data)
            
    def circular(self) -> None:
        head = self.head
        while head.next is not None:
            head = head.next
            
        head.next = self.head
            

node = Node(7)
second_node = Node(8)
third_node = Node(1)
linkedlist = LinkedList()
linkedlist.insert(node)
linkedlist.insert(second_node)
linkedlist.insert(third_node)
#linkedlist.printlist()
#print(linkedlist.size)
#print(linkedlist.list_size())
#print(linkedlist.search(10))
#print(linkedlist.get_index(1))
#print(linkedlist.insert_at(1, 5))
#linkedlist.printlist()
# linkedlist.delete_val(5)
#linkedlist.printlist()
#linkedlist.partition(1)
#linkedlist.printlist()
# linkedlist.reverse()
# linkedlist.printlist()
linkedlist.n_node(1)
linkedlist.circular()
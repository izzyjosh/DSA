from typing import Any
#singly linked list is a Data Structure that stores data that are linked together and each data has a locatiom that is placed in an entirely different place unlike list that stores data in location next to each other 
#defining a class for each node 
#A node is a class with two property (data to store and the address for the next node)

class Node:
    def __init__(self,data:Any) -> None:
        self.data = data
        self.next = None
        
# Creating the linkedlist class
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insert(self,new_node:Node) -> None:
        if self.head is None:
            self.head = new_node
        else:   
            last_node:Node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            
            last_node.next = new_node
            
    def printlist(self) -> None:
        if self.head is None:
            print("The list is empty")
        else:
            arr = []
            head = self.head
            while head is not None:
                arr.append(head.data)
                head = head.next
            print(arr)
            

    # function that print the size of the list       
    def list_size(self) -> int:
        head = self.head
        size:int = 0
        while True:
            if head is None:
                break
            else:
                size += 1
                head = head.next
        else:
            return size
        return size
        
    def search(self,data:Any) -> bool:
        head = self.head
        while True:
            if head is None:
                break
            else:
                if head.data == data:
                    return True
                head = head.next
        return False
        
    def get_index(self,index:int) -> Any:
        if index == 0 and self.head is not None:
            return self.head.data
        else:
            head = self.head          
            for i in range(index):
                head = head.next
                if head is None:
                    return "index out of range"
            return head.data
            
    def insert_at(self,index:int) -> None:
        
node = Node("hello")
second_node = Node(8)
linkedlist = LinkedList()
linkedlist.insert(node)
linkedlist.insert(second_node)
linkedlist.printlist()
print(linkedlist.list_size())
print(linkedlist.search(10))
print(linkedlist.get_index(1))
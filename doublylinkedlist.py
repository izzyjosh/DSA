from typing import Any


class Node:
    def __init__(self,value:Any) -> None:
        self.prev = None
        self.next = None
        self.data = value
 
       
class DoubleLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None
        
    def insert(self,value:Any) -> None:
        node = Node(value)
        
        if self.head is None:
            self.head = node
            self.tail = node
            
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
                
            last_node.next = node
            node.prev = last_node
            self.tail = node
        self.size += 1
        
    def printlist(self) -> None:
        head = self.head
        arr = []
        if self.head is None:
            print("empty list")
        else:
            while head is not None:
                arr.append(head.data)
                head = head.next
        print(arr)
        
    def reverse(self) -> None:
        tail = self.tail
        arr = []
        if self.tail is None:
            print("empty list:")
        else:
            while tail is not None:
                arr.append(tail.data)
                tail = tail.prev
        print(arr) 
        
              
double = DoubleLinkedList()        
double.insert(7)
double.insert([2,3])
double.insert("game")
double.insert(9)
double.printlist()
double.reverse()

# Queue is a type of data structure that follows the concept of FIFO meaning First In First Out. It can be implementedusing normal arrays or using linkedlist.

from typing import Any

class Queue:

    #Initilize the class with a know size
    #Aqueue implementated with an arr

    def __init__(self: Queue,size:int) -> None:
        self.queue = []
        self.first = 0
        self.last = 0
        self.capacity = size


    # A method to add an item to the queue

    def enqueue(self: Queue, data:Any) -> None:
        if self.last == self.capacity:
            print("Queue is full")
        else:
            self.queue.append(data)
            self.last += 1

    # Removing an element from the queue

    def dequeue(self) -> None:
        if self.first == self.last:
            print("queue is empty")
        else:
            for i in range(self.last):
                self.queue[i] = self.queue[i+1]

    # Displaying the queue items

    def display(self) -> None:
        if self.first == self.last:
            print("queue is empty")
        else:
            for i in range(self.last):
                print(self.queue[i], "<--")

queue = Queue(5)
queue.enqueue(5)
queue.enqueue("bola")
queue.display()
queue.dequeue()
queue.display()

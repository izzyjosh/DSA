class Node {
  constructor(value) {
    this.data = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.size = 0;
    this.first = null;
    this.last = null;
    this.min = this.max = null;
  }

  enqueue(data) {
    const node = new Node(data);
    if (this.size === 0 && this.first === null) {
      this.first = node;
      this.last = node;
      this.size += 1;
      this.min = this.max = node;
    } else {
      if (this.last.data < node.data) {
        this.max = node;
      } else {
        this.min = node;
      }
      this.last.next = node;
      this.last = this.last.next;
      this.size += 1;
    }
  }

  maximum() {
    console.log("the maximum is " + this.max.data);
    console.log("The minimum is " + this.min.data);
  }
  dequeue() {
    if (this.size === 0 && this.first === null) {
      console.log("Empty Queue, can't delete the first item");
    } else {
      const head = this.first.next;
      this.first = head;
      this.size -= 1;
    }
  }
  display() {
    if (this.size === 0 && this.first === null) {
      console.log("Empty queue");
    } else {
      let head = this.first;
      for (let i = 0; i < this.size; i++) {
        console.log(head.data);
        head = head.next;
      }
    }
  }
}

const queue = new LinkedList();
queue.display();
queue.enqueue(8);
queue.enqueue(9);
queue.enqueue(5);
queue.enqueue(10);
queue.display();
queue.maximum();

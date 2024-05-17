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
  }

  enqueue(data) {
    const node = new Node(data);
    if (this.size === 0 && this.first === null) {
      this.first = node;
      this.last = node;
      this.size += 1;
    } else {
      if (this.first.data < node.data) {
        const n = this.first;
        this.first = node;
        this.first.next = n;
        this.size += 1;
      } else {
        this.last.next = node;
        this.last = this.last.next;
        this.size += 1;
      }
    }
  }

  max() {
    console.log("the maximum is "+ this.first.data);
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
queue.display();
queue.max();

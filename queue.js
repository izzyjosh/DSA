class Queue {
  constructor(size) {
    this.size = size;
    this.queue = [];
    this.first = 0;
    this.last = 0;
  }

  enqueue(data) {
    if (this.last === this.size) {
      console.log("Queue is full");
    } else {
      this.queue.push(data);
      this.last += 1;
    }
  }
  dequeue() {
    if (this.first === this.last) {
      console.log("Queue is empty");
    } else {
      this.queue.map((item, i, queue) => {
        if (i === this.last - 1) {
          queue[i - 1] = queue[i];
        } else {
          queue[i] = queue[i + 1];
        }
      });
      this.queue.pop()
      this.last -= 1;
    }
  }
  display() {
    if (this.first === this.last) {
      console.log("Queue is Empty");
    } else {
      this.queue.forEach(item => {
        console.log(item + "<--");
      });
    }
  }
}

const queue = new Queue(8);
queue.display();
queue.enqueue(8);
queue.enqueue("mike");
queue.display();
queue.dequeue();
queue.display();

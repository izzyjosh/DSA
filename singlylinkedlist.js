class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
    this.list = [];
  }

  append(val) {
    const node = new Node(val);

    if (this.head === null) {
      this.head = node;
      this.size += 1;
      this.list.push(node.data);
    } else {
      let head = this.head;
      while (head.next !== null) {
        head = head.next;
      }

      head.next = node;
      this.size += 1;
      this.list.push(node.data);
    }
  }
  /* printlist() {
  if (this.head === null) {
   console.log("empty list")
  } else {
   let head = this.head
   let arr = [5]
   for (let i = 0; i < this.size; i++) {
    arr.push(head.data)
    head = head.next
   }
   console.log(arr)
  }
 }*/
}

let linkedlist = new LinkedList();

linkedlist.append(9);
linkedlist.append(8);
linkedlist.append(7);

console.log(linkedlist.list);

class Queue {
	constructor (size) {
		this.size = size
		this.queue = []
		this.first = 0
		this.last = 0
	}

	enqueue(data) {
		if (this.last === this.size) {
			console.log("Queue is full")
		}
		else {
			this.queue.push(data)
			this.last += 1
		}
	}
	dequeue() {
		if (this.first === this.last) {
			console.log("Queue is empty")
		}
		else {
			for (let i = 0;i < this.size; i++) {
				if (i === this.last - 1) {
					this.queue[i-1] = this.queue[i]
				}
				else {
					this.queue[i] = this.queue[i+1]
				}
			}
			this.last -= 1
		}
	}
	display() {
		if (this.first === this.last) {
			console.log("Queue is Empty")
		}
		else {
			for (let i = 0; i < this.last; i++) {
				console.log(this.queue[i] + "<-- ")
			}
		}
	}
}

const queue = new Queue(8)
queue.display()
queue.enqueue(8)
queue.enqueue("mike")
queue.display()
queue.dequeue()
queue.display()

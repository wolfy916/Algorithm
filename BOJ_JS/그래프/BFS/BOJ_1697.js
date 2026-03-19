/**
 * 제목 : 숨바꼭질
 * 난이도 : 실버 1
 * 분류 : BFS
 */

class Node {
  constructor(value) {
    this.value = value;
    this.nextNode = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.rear = null;
    this.size = 0;
  }

  enqueue(value) {
    const node = new Node(value);

    if (this.size == 0) {
      this.head = node;
    } else {
      this.rear.nextNode = node;
    }
    
    this.rear = node;
    
    this.size++;
  }

  dequeue() {
    if (this.size == 0) return;

    const dequeueNodeValue = this.head.value;

    if (this.size == 1) {
      this.head = null;
      this.rear = null;
    } else {
      this.head = this.head.nextNode;
    }

    this.size--;

    return dequeueNodeValue;
  }
}

const solution = (input) => {
  const [n, k] = input[0].split(" ").map(Number);

  const MAX_SIZE = 100_001;
  const visitedTimeLogs = Array.from({ length: MAX_SIZE }, () => Infinity);
  visitedTimeLogs[n] = 0;

  const queue = new Queue();
  queue.enqueue(n);

  while (queue.size > 0) {
    const v = queue.dequeue();

    if (v == k) break;

    for (const w of [v - 1, v + 1, v * 2]) {
      if (w < 0 || w >= MAX_SIZE) continue;
      if (visitedTimeLogs[v] + 1 >= visitedTimeLogs[w]) continue;
      visitedTimeLogs[w] = visitedTimeLogs[v] + 1;
      queue.enqueue(w);
    }
  }

  return visitedTimeLogs[k];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

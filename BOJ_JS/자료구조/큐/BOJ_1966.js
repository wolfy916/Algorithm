/**
 * 제목 : 프린터 큐
 * 난이도 : 실버 3
 * 분류 : 구현, 자료구조, 시뮬레이션, 큐
 */

class Node {
  constructor(value, index, nextNode) {
    this.value = value;
    this.index = index;
    this.nextNode = nextNode;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.rear = null;
    this.size = 0;
  }

  enqueue(value, index) {
    const node = new Node(value, index, null);

    if (!this.head) {
      this.head = this.rear = node;
    } else {
      this.rear.nextNode = node;
      this.rear = node;
    }

    this.size++;
  }

  dequeue() {
    if (this.size < 1) throw Error("This queue is empty.");

    const result = [this.head.value, this.head.index];

    if (this.head.nextNode != null) {
      this.head = this.head.nextNode;
    } else {
      this.head = null;
      this.rear = null;
    }

    this.size--;

    return result;
  }
}

const convertToNumberArray = (str) => str.split(" ").map(Number);

const solution = (input) => {
  const testCase = Number(input[0]);
  const answer = [];

  let line = 1;
  const count = Array.from({ length: 10 }, () => 0);
  for (let i = 0; i < testCase; i++) {
    count.fill(0);

    const [n, m] = convertToNumberArray(input[line++]);
    const priorities = convertToNumberArray(input[line++]);
    const queue = new Queue();

    priorities.forEach((v, i) => {
      count[v]++;
      queue.enqueue(v, i);
    });

    let indexOfMaxPriority = 9;
    let printOrder = 1;
    while (queue.size > 0) {
      const [currentPriority, currentIndex] = queue.dequeue();

      while (indexOfMaxPriority > 0 && count[indexOfMaxPriority] < 1) {
        indexOfMaxPriority--;
      }

      if (currentPriority == indexOfMaxPriority) {
        if (currentIndex == m) {
          answer.push(printOrder);
          break;
        }
        count[currentPriority]--;
        printOrder++;
      } else {
        queue.enqueue(currentPriority, currentIndex);
      }
    }
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

/**
 * 제목 : 중력 큐
 * 난이도 : 실버 1
 * 분류 : 구현
 */

class Node {
  constructor(value, prevNode = null, nextNode = null) {
    this.value = value;
    this.prevNode = prevNode;
    this.nextNode = nextNode;
  }
}

class Dequeue {
  constructor() {
    this.head = null;
    this.rear = null;
    this.size = 0;
  }

  push(value) {
    const node = new Node(value);

    if (this.size < 1) {
      this.head = node;
      this.rear = node;
    } else {
      this.rear.nextNode = node;
      node.prevNode = this.rear;
      this.rear = node;
    }

    this.size++;
  }

  pop() {
    if (this.size === 0) throw Error("Dequeue is empty.");

    const popNode = this.rear;

    if (this.size === 1) {
      this.head = null;
      this.rear = null;
    } else {
      this.rear = this.rear.prevNode;
      this.rear.nextNode = null;
    }

    this.size--;

    return popNode.value;
  }

  shift() {
    if (this.size === 0) throw Error("Dequeue is empty.");

    const popNode = this.head;

    if (this.size === 1) {
      this.head = null;
      this.rear = null;
    } else {
      this.head = this.head.nextNode;
      this.head.prevNode = null;
    }

    this.size--;

    return popNode.value;
  }
}

const solution = (input) => {
  const numberOfQueries = Number(input[0]);

  const state = ["right", "down", "left", "up"];
  let stateIdx = 0;
  const rotate = {
    l: () => {
      if (stateIdx === 0) stateIdx = 3;
      else stateIdx--;
    },
    r: () => (stateIdx = (stateIdx + 1) % 4),
  };

  const dequeue = new Dequeue();

  let countW = 0;
  const countB = () => dequeue.size - countW;

  const pourOut = () => {
    if (state[stateIdx] === "up") {
      while (dequeue.size > 0 && dequeue.rear.value === "b") {
        dequeue.pop();
      }
    } else if (state[stateIdx] === "down") {
      while (dequeue.size > 0 && dequeue.head.value === "b") {
        dequeue.shift();
      }
    }
  };

  const output = [];

  for (let i = 1; i < numberOfQueries + 1; i++) {
    const [command, type] = input[i].split(" ");
    switch (command) {
      case "push":
        if (type === "b") {
          if (state[stateIdx] === "up") break;
          if (state[stateIdx] === "down" && countW < 1) break;
          dequeue.push(type);
        } else {
          countW++;
          dequeue.push(type);
        }
        break;
      case "pop":
        if (dequeue.size > 0) {
          const popValue = dequeue.shift();
          if (popValue === "w") countW--;
        }
        pourOut();
        break;
      case "rotate":
        rotate[type]();
        pourOut();
        break;
      case "count":
        output.push(type === "w" ? countW : countB());
        break;
    }
  }

  return output.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

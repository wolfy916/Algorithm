/**
 * 제목 : 스택 수열
 * 난이도 : 실버 2
 * 분류 : 스택, 구현
 */

class Stack {
  constructor() {
    this.top = -1;
    this.stack = {};
    this.size = 0;
  }

  insert(x) {
    this.stack[++this.top] = x;
    this.size++;
  }

  pop() {
    if (this.size < 1) return null;
    const popData = this.stack[this.top];
    delete this.stack[this.top--];
    this.size--;
    return popData;
  }

  get getTop() {
    if (this.size < 1) return 0;
    else return this.stack[this.top];
  }
}

const solution = (input) => {
  const N = Number(input[0]);
  const arr = input.slice(1).map(Number);
  const answer = [];
  const stack = new Stack();
  let num = 1;
  let i = -1;

  while (++i < N) {
    while (stack.getTop < arr[i]) {
      stack.insert(num++);
      answer.push("+");
    }

    if (stack.getTop === arr[i]) {
      stack.pop();
      answer.push("-");
    } else return "NO";
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
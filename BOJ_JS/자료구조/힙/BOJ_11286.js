/**
 * 제목 : 절댓값 힙
 * 난이도 : 실버 1
 * 분류 : 힙
 */

/**
 * 접근 방식
 * 1. 힙 메소드 구현
 */

const heappush = (heap, data) => {
  heap.push(data);
  current = heap.length - 1;
  while (current > 0) {
    parent = Math.floor((current - 1) / 2);
    if (Math.abs(heap[parent]) > Math.abs(heap[current])) {
      [heap[parent], heap[current]] = [heap[current], heap[parent]];
      current = parent;
    } else if (Math.abs(heap[parent]) === Math.abs(heap[current])) {
      if (heap[parent] > heap[current]) {
        [heap[parent], heap[current]] = [heap[current], heap[parent]];
        current = parent;
      } else break;
    } else break;
  }
};

const heappop = (heap) => {
  if (heap.length < 1) return 0;
  else if (heap.length === 1) return heap.pop();

  [pop_data, heap[0]] = [heap[0], heap.pop()];
  [current, child] = [0, 1];
  while (child < heap.length) {
    sibling = child + 1;
    if (
      sibling < heap.length &&
      Math.abs(heap[child]) > Math.abs(heap[sibling])
    ) {
      child = sibling;
    } else if (
      sibling < heap.length &&
      Math.abs(heap[child]) === Math.abs(heap[sibling])
    ) {
      if (heap[child] > heap[sibling]) {
        child = sibling;
      }
    }
    if (Math.abs(heap[current]) > Math.abs(heap[child])) {
      [heap[current], heap[child]] = [heap[child], heap[current]];
      current = child;
      child = current * 2 + 1;
    } else if (Math.abs(heap[current]) === Math.abs(heap[child])) {
      if (heap[current] > heap[child]) {
        [heap[current], heap[child]] = [heap[child], heap[current]];
        current = child;
        child = current * 2 + 1;
      } else break;
    } else break;
  }

  return pop_data;
};

const solution = (input) => {
  const [_, ...inputArr] = input.map((v) => +v);
  const numArr = [];
  const answer = [];
  for (let x of inputArr) {
    if (x === 0) {
      answer.push(heappop(numArr));
    } else {
      heappush(numArr, x);
    }
  }
  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
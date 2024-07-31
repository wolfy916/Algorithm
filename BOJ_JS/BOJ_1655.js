/**
 * 제목 : 가운데를 말해요
 * 난이도 : 골드 2
 * 분류 : 우선순위 큐
 */

const priorityQueue = () => {
  const maxHeap = [];
  const minHeap = [];

  const change = (arr, x, y) => {
    const tmp = arr[x];
    arr[x] = arr[y];
    arr[y] = tmp;
  }

  const topDown = (arr, isMaxHeap) => {
    let cur = 0;
    let chd = cur * 2 + 1;
    let sibling;
    while (chd < arr.length) {
      sibling = chd + 1;
      if (sibling < arr.length) {
        if (isMaxHeap && arr[chd] < arr[sibling]) {
          chd = sibling;
        } else if (!isMaxHeap && arr[chd] > arr[sibling]) {
          chd = sibling;
        }
      }

      if (isMaxHeap) {
        if (arr[cur] < arr[chd]) {
          change(maxHeap, cur, chd);
          cur = chd;
          chd = cur * 2 + 1;
        } else break;
      } else {
        if (arr[cur] > arr[chd]) {
          change(minHeap, cur, chd);
          cur = chd;
          chd = cur * 2 + 1;
        } else break;
      }
    }
  }

  const bottomUp = (arr, isMaxHeap) => {
    let cur = arr.length - 1;
    let par;
    while (cur > 0) {
      par = Math.floor((cur - 1) / 2);
      if (isMaxHeap) {
        if (arr[par] < arr[cur]) {
          change(arr, par, cur);
          cur = par;
        } else break;
      } else {
        if (arr[par] > arr[cur]) {
          change(arr, par, cur);
          cur = par;
        } else break;
      }
    }
  }

  const enqueue = (x) => {
    if (maxHeap.length === 0) {
      maxHeap.push(x);
      return;
    }

    if (x > maxHeap[0]) {
      minHeap.push(x);
      bottomUp(minHeap, false);
    } else {
      maxHeap.push(x);
      bottomUp(maxHeap, true);
    }

    if (minHeap.length > maxHeap.length) {
      maxHeap.push(dequeue(minHeap, false));
      bottomUp(maxHeap, true);
    } else if (minHeap.length + 1 < maxHeap.length) {
      minHeap.push(dequeue(maxHeap, true));
      bottomUp(minHeap, false);
    }
  }

  const dequeue = (arr, isMaxHeap) => {
    if (arr.length === 0) return null;
    if (arr.length === 1) return arr.pop();

    const popData = arr[0];
    arr[0] = arr.pop();
    topDown(arr, isMaxHeap);
    
    return popData;
  }

  const getValue = () => maxHeap[0];

  return {
    enqueue,
    getValue,
  }
}

const solution = (input) => {
  const N = Number(input[0]);
  const answer = [];
  const { enqueue, getValue } = priorityQueue();

  for (let i=1; i<N+1; i++) {
    const num = Number(input[i]);
    enqueue(num);
    answer.push(getValue());
  }

  return answer.join('\n');
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
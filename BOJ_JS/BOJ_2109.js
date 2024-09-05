/**
 * 제목 : 순회강연
 * 난이도 : 골드 3
 * 분류 : 그리디, 우선 순위 큐
 */

const minHeap = () => {
  const arr = [];

  const change = (x, y) => {
    const tmp = arr[x];
    arr[x] = arr[y];
    arr[y] = tmp;
  };

  const bottomUp = () => {
    let cur = arr.length - 1;
    let par;
    while (cur > 0) {
      par = Math.floor((cur - 1) / 2);
      if (arr[cur] < arr[par]) {
        change(cur, par);
        cur = par;
      } else break;
    }
  };

  const push = (x) => {
    arr.push(x);
    bottomUp();
  };

  const topDown = () => {
    let cur = 0;
    let chd = 1;
    let sibling;
    while (chd < arr.length) {
      chd = cur * 2 + 1;
      sibling = chd + 1;
      if (sibling < arr.length && arr[chd] > arr[sibling]) {
        chd = sibling;
      }
      if (arr[cur] > arr[chd]) {
        change(cur, chd);
        cur = chd;
      } else break;
    }
  };

  const pop = () => {
    if (arr.length === 1) return arr.pop();
    const popData = arr[0];
    arr[0] = arr.pop();
    topDown();
    return popData;
  };

  const getTop = () => arr[0];

  const getSumV = () => arr.reduce((a, c) => a + c);

  return {
    push,
    pop,
    getTop,
    getSumV,
  };
};

const solution = (input) => {
  const N = Number(input[0]);
  if (N === 0) return 0;
  const schedule = input.slice(1).map((v) => v.split(" ").map(Number));
  
  schedule.sort((a, b) => a[1] - b[1]);

  let time = 1;
  const { getTop, push, pop, getSumV } = minHeap();
  push(schedule[0][0]);

  for (let i = 1; i < N; i++) {
    const [p, d] = schedule[i];
    if (time < d) {
      push(p);
      time++;
    } else {
      if (getTop() < p) {
        pop();
        push(p);
      }
    }
  }

  return getSumV();
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
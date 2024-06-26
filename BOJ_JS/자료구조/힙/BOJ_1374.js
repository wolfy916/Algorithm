/**
 * 제목 : 강의실
 * 난이도 : 골드5
 * 분류 : 정렬, 우선순위 큐
 */

const minHeap = () => {
  const arr = [];

  const change = (a, b) => {
    const temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
  }

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
  }

  const push = (x) => {
    arr.push(x);
    bottomUp();
  }

  const topDown = () => {
    let cur = 0;
    let chd = cur * 2 + 1;
    let sibling;
    while (chd < arr.length) {
      sibling = chd + 1;
      if (sibling < arr.length && arr[sibling] < arr[chd]) {
        chd = sibling;
      }

      if (arr[chd] < arr[cur]) {
        change(chd, cur);
        cur = chd;
        chd = chd * 2 + 1;
      } else break;
    }
  }

  const pop = () => {
    if (arr.length === 0) return null;
    if (arr.length === 1) return arr.pop();

    const popData = arr[0];
    arr[0] = arr.pop();

    topDown();

    return popData;
  }

  const size = () => arr.length;

  const top = () => arr[0];

  return {
    push,
    pop,
    size,
    top,
  }
}

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const N = convert(input[0]);
  const info = input.slice(1,).map(convert);

  info.sort((a, b) => {
    if (a[1] === b[1]) return a[2] - b[2];
    else return a[1] - b[1];
  });

  let answer = 1;
  const { push, pop, size, top } = minHeap();
  push(info[0][2]);

  for (let i=1; i<N; i++) {
    while (top() <= info[i][1]) pop();
    push(info[i][2]);
    if (answer < size()) answer = size();
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
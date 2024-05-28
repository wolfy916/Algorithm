/**
 * 제목 : 두 로봇
 * 난이도 : 골드 4
 * 분류 : 다잌스트라
 */

class MinHeap {
  constructor() {
    this.arr = [];
  }

  push(x) {
    this.arr.push(x);
    this.bottomUp();
  }

  pop() {
    if (this.arr.length < 1) return null;
    if (this.arr.length < 2) return this.arr.pop();
    let popData;
    [popData, this.arr[0]] = [this.arr[0], this.arr.pop()];
    this.topDown();
    return popData;
  }

  topDown() {
    let par = 0;
    let chd = par * 2 + 1;
    while (chd < this.arr.length) {
      let sibling = chd + 1;
      if (sibling < this.arr.length && this.arr[sibling] < this.arr[chd]) {
        chd = sibling;
      }
      if (this.arr[chd][1] < this.arr[par][1]) {
        this.change(chd, par);
        par = chd;
      } else return;
    }
  }

  bottomUp() {
    let chd = this.arr.length - 1;
    while (chd > 0) {
      let par = Math.floor((chd - 1) / 2);
      if (this.arr[chd][1] < this.arr[par][1]) {
        this.change(chd, par);
        chd = par;
      } else return;
    }
  }

  change(chd, par) {
    [this.arr[chd], this.arr[par]] = [this.arr[par], this.arr[chd]];
  }

  length() {
    return this.arr.length;
  }
}

const converToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [[N, A, B], edges] = [
    converToNumArr(input[0]),
    input.slice(1,).map(v => converToNumArr(v)),
  ];

  const adjL = Array.from({length: N + 1}, () => []);
  for (let i=0; i<edges.length; i++) {
    const [u, v, w] = edges[i];
    adjL[u].push([v, w]);
    adjL[v].push([u, w]);
  }

  const visited = Array.from({length: N + 1}, () => false);
  const minHeap = new MinHeap();
  visited[A] = true;
  minHeap.push([A, 0, 0]);
  while (minHeap.length() > 0) {
    const [v, w, maxV] = minHeap.pop();
    if (v === B) {
      return w - maxV;
    }
    for (const [nv, nw] of adjL[v]) {
      if (visited[nv]) continue;
      visited[nv] = true;
      minHeap.push([nv, w + nw, Math.max(maxV, nw)]);
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
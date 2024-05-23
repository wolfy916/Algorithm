/**
 * 제목 : 최단경로
 * 난이도 : 골드4
 * 분류 : dijkstra
 */

/**
 * 과정
 * 1. 플로이드 워셜의 3중 for문, 인접행렬은 바로 터질 것 같은 사이즈
 * 2. 자료구조 없이 인접리스트와 dijkstra 함수를 구현했더니 시간초과
 * 3. 체념하고 link랑 MinHeap 구현
 */

class MinHeap {
  constructor() {
    this.arr = [];
  }

  topDown() {
    let par = 0;
    let chd = par * 2 + 1;
    while (chd < this.arr.length) {
      let sibling = chd + 1;
      if (
        sibling < this.arr.length &&
        this.arr[sibling][1] < this.arr[chd][1]
      ) {
        chd = sibling;
      }
      if (!this.change(par, chd)) break;
      [par, chd] = [chd, par * 2 + 1];
    }
  }

  bottomUp() {
    let chd = this.arr.length - 1;
    while (chd > 0) {
      let par = Math.floor((chd - 1) / 2);
      if (!this.change(par, chd)) break;
      chd = par;
    }
  }

  change(par, chd) {
    if (this.arr[par][1] > this.arr[chd][1]) {
      [this.arr[par], this.arr[chd]] = [this.arr[chd], this.arr[par]];
      return true;
    } else return false;
  }

  push(x) {
    this.arr.push(x);
    this.bottomUp();
  }

  pop() {
    if (this.arr.length === 0) return null;
    if (this.arr.length === 1) return this.arr.pop();
    let pop_data;
    [pop_data, this.arr[0]] = [this.arr[0], this.arr.pop()];
    this.topDown();
    return pop_data;
  }

  length() {
    return this.arr.length;
  }

  array() {
    return this.arr;
  }
}

const convertToNumArr = (strArr) => strArr.split(" ").map((v) => +v);

const solution = (input) => {
  const [[V, _], K, edges] = [
    convertToNumArr(input[0]),
    +input[1],
    input.slice(2).map((v) => convertToNumArr(v)),
  ];

  const link = Array.from({ length: V + 1 }, () => []);
  edges.forEach(([u], idx) => link[u].push(idx));

  const minHeap = new MinHeap();
  minHeap.push([K, 0]);

  const dist = Array(V + 1).fill(Infinity);
  dist[K] = 0;

  while (minHeap.length() > 0) {
    const [curV, curW] = minHeap.pop();
    if (dist[curV] < curW) continue;

    for (let i of link[curV]) {
      const [_, nxtV, nxtW] = edges[i];
      const newW = curW + nxtW;

      if (dist[nxtV] > newW) {
        dist[nxtV] = newW;
        minHeap.push([nxtV, newW]);
      }
    }
  }

  return dist
    .slice(1)
    .map((v) => (v === Infinity ? "INF" : v))
    .join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
/**
 * 제목 : 간선 이어가기 2
 * 난이도 : 골드 5
 * 분류 : 다잌스트라
 */

class MinHeap {
  constructor() {
    this.heap = [[null, null]];
  }

  size() {
    return this.heap.length - 1;
  }

  exchange(a, b) {
    const tmp = this.heap[a];
    this.heap[a] = this.heap[b];
    this.heap[b] = tmp;
  }

  bottomUp() {
    let cur = this.size();
    let par;
    while (cur > 0) {
      par = cur >> 1;
      if (this.heap[cur][1] < this.heap[par][1]) {
        this.exchange(cur, par);
        cur = par;
      } else break;
    }
  }

  topDown() {
    let cur = 1;
    let chd = 2;
    let sibling;
    while (chd < this.size()) {
      sibling = chd + 1;
      if (
        sibling < this.size() && 
        this.heap[sibling][1] < this.heap[chd][1]
      ) {
        chd = sibling;
      }
      if (this.heap[chd][1] < this.heap[cur][1]) {
        this.exchange(chd, cur);
        cur = chd;
        chd = cur << 1;
      } else break;
    }
  }

  push(edge) {
    this.heap.push(edge);
    this.bottomUp();
  }

  pop() {
    if (this.size() == 1) return this.heap.pop();

    const result = this.heap[1];
    this.heap[1] = this.heap.pop();
    this.topDown();

    return result;
  }
}

const solution = (input) => {

  const convert = (s) => s.split(" ").map(Number);
  const [n, m] = convert(input[0]);
  const [s, t] = convert(input[m + 1]);
  
  const adjList = Array.from({ length: n + 1 }, () => []);
  for (let i=1; i<m + 1; i++) {
    const [a, b, c] = convert(input[i]);
    adjList[a].push([b, c]);
    adjList[b].push([a, c]);
  }

  const minHeap = new MinHeap();
  const distance = Array.from({ length: n + 1 }, () => Infinity);
  
  distance[s] = 0;
  minHeap.push([s, 0]);

  while(minHeap.size() > 0) {
    const [v, _] = minHeap.pop();
    for (const [n, nw] of adjList[v]) {
      if (distance[v] + nw >= distance[n]) continue;
      distance[n] = distance[v] + nw;
      minHeap.push([n, distance[n]]);
    }
  }

  return distance[t];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
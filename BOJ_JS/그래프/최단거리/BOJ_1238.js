/**
 * 제목 : 파티
 * 난이도 : 골드 3
 * 분류 : dijkstra
 */

class MinHeap {
  constructor() {
    this.heap = [];
  }

  change(x, y) {
    const tmp = this.heap[x];
    this.heap[x] = this.heap[y];
    this.heap[y] = tmp;
  }

  bottomUp() {
    let cur = this.heap.length - 1;
    let par;
    while (cur > 0) {
      par = Math.floor((cur - 1) / 2);
      if (this.heap[cur][1] < this.heap[par][1]) {
        this.change(cur, par);
        cur = par;
      } else break;
    }
  }

  push(x) {
    this.heap.push(x);
    this.bottomUp();
  }

  topDown() {
    let cur = 0;
    let chd = 1;
    let sibling;
    while (chd < this.heap.length) {
      sibling = chd + 1;
      if (sibling < this.heap.length && this.heap[sibling][1] < this.heap[chd][1]) {
        chd = sibling;
      }

      if (this.heap[chd][1] < this.heap[cur][1]) {
        this.change(cur, chd);
        cur = chd;
        chd = cur * 2 + 1;
      } else break;
    }
  }

  pop() {
    if (this.heap.length === 1) return this.heap.pop();
    const popData = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.topDown();
    return popData;
  }
}

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M, X] = convert(input[0]);
  const adjL1 = Array.from(Array(N + 1), () => []);
  const adjL2 = Array.from(Array(N + 1), () => []);
  
  for (let i=1; i<M + 1; i++) {
    const [A, B, T] = convert(input[i]);
    adjL1[A].push([B, T]);
    adjL2[B].push([A, T]);
  }

  const distance1 = dijkstra(X, 1);
  const distance2 = dijkstra(X, 2);

  distance1[0] = 0;
  distance2[0] = 0;

  return Math.max(...Array.from(Array(N + 1), (_, i) => distance1[i] + distance2[i]));

  function dijkstra(s, num) {
    const D = Array(N + 1).fill(Infinity);
    const minHeap = new MinHeap();

    minHeap.push([s, 0]);
    D[s] = 0;
    
    while (minHeap.heap.length > 0) {
      const [v, vd] = minHeap.pop();
      for (const [w, wd] of num > 1 ? adjL2[v] : adjL1[v]) {
        if (D[v] + wd >= D[w]) continue;
        D[w] = D[v] + wd;
        minHeap.push([w, wd]);
      }
    }

    return D;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
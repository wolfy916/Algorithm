/**
 * 제목 : 엔터프라이즈호 탈출
 * 난이도 : 골드 4
 * 분류 : 최단 경로, 데이크스트라
 */

class MinHeap {
  constructor() {
    this.heap = [null];
  }

  get size() {
    return this.heap.length - 1;
  }

  getPar(chd) {
    return chd >> 1;
  }

  getLeftChd(par) {
    return par << 1;
  }

  change(x, y) {
    const tmp = this.heap[x];
    this.heap[x] = this.heap[y];
    this.heap[y] = tmp;
  }

  bottomUp() {
    let cur = this.heap.length - 1;
    let par;
    while (cur > 1) {
      par = this.getPar(cur);
      if (this.heap[cur][2] < this.heap[par][2]) {
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
    let cur = 1;
    let chd = 2;
    let sibling;
    while (chd < this.heap.length) {
      sibling = chd + 1;
      if (
        sibling < this.heap.length &&
        this.heap[sibling][2] < this.heap[chd][2]
      ) {
        chd = sibling;
      }
      if (this.heap[chd][2] < this.heap[cur][2]) {
        this.change(chd, cur);
        cur = chd;
        chd = this.getLeftChd(cur);
      } else break;
    }
  }

  pop() {
    if (this.size === 1) return this.heap.pop();

    const data = this.heap[1];
    this.heap[1] = this.heap.pop();
    this.topDown();

    return data;
  }
}

const solution = (input) => {
  const answer = [];
  const T = Number(input[0]);
  const timeMap = new Map();

  let line = 1;
  for (let t = 0; t < T; t++) {
    const [K, W, H] = input[line++].split(" ").map(Number);

    timeMap.clear();
    timeMap.set("E", 0);

    for (let k = 0; k < K; k++) {
      const [shipName, needTime] = input[line++].split(" ");
      timeMap.set(shipName, Number(needTime));
    }

    const board = Array.from({ length: H }, () => input[line++]);
    const visited = Array.from({ length: H }, () => Array(W).fill(Infinity));
    const di = [-1, 1, 0, 0];
    const dj = [0, 0, -1, 1];
    const isEdge = (i, j) => i === 0 || j === 0 || i === H - 1 || j === W - 1;

    let si, sj;
    outer: for (let i = 0; i < H; i++) {
      for (let j = 0; j < W; j++) {
        if (board[i][j] === "E") {
          si = i;
          sj = j;
          break outer;
        }
      }
    }

    const priorityQueue = new MinHeap();
    priorityQueue.push([si, sj, 0]);
    visited[si][sj] = 0;

    dijkstra: while (priorityQueue.size > 0) {
      const [vi, vj, vt] = priorityQueue.pop();

      if (isEdge(vi, vj)) {
        answer.push(vt);
        break dijkstra;
      }

      for (let k = 0; k < 4; k++) {
        const ni = vi + di[k];
        const nj = vj + dj[k];
        const nt = vt + timeMap.get(board[ni][nj]);

        if (visited[ni][nj] <= nt) continue;

        visited[ni][nj] = nt;
        priorityQueue.push([ni, nj, nt]);
      }
    }
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
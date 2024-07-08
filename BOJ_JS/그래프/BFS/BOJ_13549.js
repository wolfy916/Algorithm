/**
 * 제목 : 숨바꼭질 3
 * 난이도 : 골드 5
 * 분류 : bfs, 다잌스트라
 */

const minHeap = () => {
  const heap = [];

  const change = (x, y) => {
    const tmp = [...heap[x]];
    heap[x] = [...heap[y]];
    heap[y] = [...tmp];
  }

  const push = (x) => {
    heap.push(x);
    
    let cur = heap.length - 1;
    let par;
    while (cur > 0) {
      par = Math.floor((cur - 1) / 2);
      if (heap[cur][0] < heap[par][0]) {
        change(cur, par);
        cur = par;
      } else break;
    }
  }

  const pop = () => {
    if (heap.length < 1) return null;
    if (heap.length === 1) return heap.pop();

    const popData = [...heap[0]];
    heap[0] = heap.pop();

    let cur = 0;
    let chd = cur * 2 + 1;
    let sibling;
    while (chd < heap.length) {
      sibling = chd + 1;
      if (sibling < heap.length && heap[sibling][0] < heap[chd][0]) {
        chd = sibling;
      }

      if (heap[chd][0] < heap[cur][0]) {
        change(chd, cur);
        cur = chd;
        chd = chd * 2 + 1;
      } else break;
    }

    return popData;
  }

  const getLength = () => heap.length;

  return {
    push,
    pop,
    getLength,
  }
}

const solution = (input) => {
  const [N, K] = input[0].split(" ").map(Number);
  return bfs(N, K);

  function bfs(n, k) {
    const visited = Array.from({ length: 1e5 + 1 }, () => Infinity);
    const { push, pop, getLength } = minHeap();
    visited[n] = 0;
    push([0, n]);

    if (0 < n) {
      n *= 2;
      while (n <= 1e5) {
        visited[n] = 0;
        push([0, n]);
        n *= 2;
      }
    }

    while (getLength() > 0) {
      const [t, v] = pop();
      if (v === k) return t;
      for (const w of [v - 1, v + 1]) {
        if (w < 0 || w > 1e5) continue;
        if (visited[w] <= t + 1) continue;
        visited[w] = t + 1;
        push([visited[w], w]);

        let double = w * 2;
        while (0 < double && double <= 1e5) {
          if (visited[double] > visited[w]) {
            visited[double] = visited[w];
            push([visited[w], double]);
          }
          double *= 2;
        }
      }
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
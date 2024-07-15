/**
 * 제목 : 택배 배송
 * 난이도 : 골드 5
 * 분류 : 다잌스트라
 */

const minHeap = () => {
  const heap = [];

  const change = (x, y) => {
    const tmp = heap[x];
    heap[x] = heap[y];
    heap[y] = tmp;
  }

  const bottomUp = () => {
    let cur = heap.length - 1;
    let par;
    while (cur > 0) {
      par = Math.floor((cur - 1) / 2);
      if (heap[cur][1] < heap[par][1]) {
        change(cur, par);
        cur = par;
      } else break;
    }
  }

  const push = (x) => {
    heap.push(x);
    bottomUp();
  }

  const topDown = () => {
    let cur = 0;
    let chd = cur * 2 + 1;
    let sibling;
    while (chd < heap.length) {
      sibling = chd + 1;
      if (sibling < heap.length && heap[sibling][1] < heap[chd][1]) {
        chd = sibling;
      }
      
      if (heap[chd][1] < heap[cur][1]) {
        change(chd, cur);
        cur = chd;
        chd = cur * 2 + 1;
      } else break;
    }
  }

  const pop = () => {
    if (heap.length === 0) return null;
    if (heap.length === 1) return heap.pop();
    
    const popData = heap[0];
    heap[0] = heap.pop();
    topDown();
    
    return popData;
  }

  return {
    push,
    pop,
    heap,
  }
}

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, M]= convert(input[0]);
  const adjL = Array.from({ length: N + 1 }, () => []);

  for (let i=1; i<M + 1; i++) {
    const [a, b, c] = convert(input[i]);
    adjL[a].push([b, c]);
    adjL[b].push([a, c]);
  }

  return dijkstra();

  function dijkstra() {
    const distance = Array.from({ length: N + 1 }, () => Infinity);
    const { heap, push, pop } = minHeap();
    distance[1] = 0;
    push([1, 0]);
    while (heap.length > 0) {
      const [v, vc] = pop();
      if (v === N) return vc;
      for (let [w, wc] of adjL[v]) {
        if (distance[w] > distance[v] + wc) {
          distance[w] = distance[v] + wc
          push([w, distance[w]]);
        }
      }
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split('\n');
console.log(solution(input));
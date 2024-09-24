/**
 * 제목 : 미로 만들기
 * 난이도 : 골드 4
 * 분류 : 다잌스트라, BFS
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
      if (heap[cur][2] < heap[par][2]) {
        change(cur, par);
        cur = par;
      } else break;
    }
  }

  const insert = (i, j, cnt) => {
    heap.push([i, j, cnt]);
    bottomUp();
  }

  const topDown = () => {
    let cur = 0;
    let chd = 1;
    let sibling;
    while (chd < heap.length) {
      sibling = chd + 1;
      if (sibling < heap.length && heap[sibling][2] < heap[chd][2]) {
        chd = sibling;
      }

      if (heap[chd][2] < heap[cur][2]) {
        change(chd, cur);
        cur = chd;
        chd = cur * 2 + 1;
      } else break;
    }
  }

  const popLeft = () => {
    if (heap.length === 1) return heap.pop();

    const popData = heap[0];
    heap[0] = heap.pop();
    topDown();

    return popData;
  }

  const size = () => heap.length;

  return {
    insert,
    popLeft,
    size,
    heap,
  }
}

const solution = (input) => {
  const N = Number(input.shift());
  const visited = Array.from(Array(N), () => Array(N).fill(false));
  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];

  return bfs(0, 0);

  function bfs(si, sj) {
    const pq = minHeap();
    visited[si][sj] = true;
    pq.insert(si, sj, 0);

    let vi, vj, cnt;
    while (pq.size() > 0) {
      [vi, vj, cnt] = pq.popLeft();
      if (vi === N - 1 && vj === N - 1) return cnt;

      let ni, nj;
      for (let k = 0; k < 4; k++) {
        ni = vi + di[k];
        nj = vj + dj[k];
        if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
        if (visited[ni][nj]) continue;
        visited[ni][nj] = true;
        pq.insert(ni, nj, input[ni][nj] === '0' ? cnt + 1 : cnt);
      }
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
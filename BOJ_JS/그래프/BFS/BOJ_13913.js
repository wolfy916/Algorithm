/**
 * 제목 : 숨바꼭질 4
 * 난이도 : 골드 4
 * 분류 : bfs
 */


const solution = (input) => {
  const [N, K] = input[0].split(" ").map(Number);
  
  const bfs = (s) => {
    const MAX = 100001;
    const visited = Array.from({ length: MAX }, () => -1);
    visited[s] = s;
    const queue = [s];
    while (queue.length > 0) {
      const v = queue.shift();
      if (v === K) break;
      for (const w of [v * 2, v + 1, v - 1]) {
        if (w < 0 || w >= MAX) continue;
        if (visited[w] >= 0) continue;
        visited[w] = v;
        queue.push(w);
      }
    }

    const path = [];
    let idx = K;
    while (visited[idx] !== idx) {
      path.push(idx);
      idx = visited[idx];
    }
    path.push(N);

    return (path.length - 1) + '\n' + path.reverse().join(' ');
  }

  return bfs(N);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
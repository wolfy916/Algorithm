/**
 * 제목 : 특정 거리의 도시 찾기
 * 난이도 : 실버 2
 * 분류 : BFS
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M, K, X] = convert(input[0]);
  const graph = Array.from(Array(N + 1), () => []);
  const visited = Array(N + 1).fill(Infinity);

  for (let i = 1; i < M + 1; i++) {
    const [A, B] = convert(input[i]);
    graph[A].push(B);
  }

  BFS([X]);

  const answer = [];
  for (let i = 1; i < N + 1; i++) {
    if (visited[i] !== K) continue;
    answer.push(i);
  }

  return answer.length > 0 ? answer.join("\n") : -1;

  function BFS(queue) {
    visited[X] = 0;
    let v;
    while (queue.length > 0) {
      v = queue.shift();
      for (const w of graph[v]) {
        if (visited[w] <= visited[v] + 1) continue;
        visited[w] = visited[v] + 1;
        queue.push(w);
      }
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
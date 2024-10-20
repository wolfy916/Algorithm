/**
 * 제목 : 촌수계산
 * 난이도 : 실버2
 * 분류 : BFS
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const N = Number(input[0]);
  const [a, b] = convert(input[1]);
  const M = Number(input[2]);
  const graph = Array.from(Array(N + 1), () => []);

  for (let i = 3; i < M + 3; i++) {
    const [x, y] = convert(input[i]);
    graph[x].push(y);
    graph[y].push(x);
  }

  let answer = -1;
  const queue = [[a, 0]];
  const visited = Array(N + 1).fill(false);
  visited[a] = true;
  while (queue.length > 0) {
    const [v, c] = queue.shift();
    if (v === b) {
      answer = c;
      break;
    }

    for (const w of graph[v]) {
      if (visited[w]) continue;
      visited[w] = true;
      queue.push([w, c + 1]);
    }
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
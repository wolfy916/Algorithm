/**
 * 제목 : DFS와 BFS
 * 난이도 : 실버2
 * 분류 : dfs, bfs
 */

/**
 * 접근 방식
 * 1. 스택과 큐를 활용한 dfs 및 bfs 구현
 */

const convertToNumArr = (strArr) => {
  return strArr.split(" ").map((v) => +v);
};

const dfs = (N, V, adjL) => {
  const visited = Array.from({ length: N + 1 }, () => false);
  const path = [];
  const stack = [V];
  while (stack.length > 0) {
    const v = stack.pop();
    if (visited[v]) continue;
    visited[v] = true;
    path.push(v);
    for (const w of adjL[v].sort((a, b) => b - a)) {
      stack.push(w);
    }
  }
  return path.join(" ");
};

const bfs = (N, V, adjL) => {
  const visited = Array.from({ length: N + 1 }, () => false);
  const path = [];
  const queue = [V];
  while (queue.length > 0) {
    const v = queue.shift();
    if (visited[v]) continue;
    visited[v] = true;
    path.push(v);
    for (const w of adjL[v].sort((a, b) => a - b)) {
      queue.push(w);
    }
  }
  return path.join(" ");
};

const solution = (input) => {
  const [firstLine, ...etcLines] = input;
  const [N, _, V] = convertToNumArr(firstLine);

  const adjL = Array.from({ length: N + 1 }, () => []);
  for (const line of etcLines) {
    const [a, b] = convertToNumArr(line);
    adjL[a].push(b);
    adjL[b].push(a);
  }

  const answer = [];
  answer.push(dfs(N, V, adjL));
  answer.push(bfs(N, V, adjL));

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
/**
 * 제목 : 연결 요소의 개수
 * 난이도 : 실버 2
 * 분류 : dfs
 */

const solution = (input) => {
  let line = 0;
  const [N, M] = input[line++].split(" ").map(Number);
  
  const graph = Array.from({ length: N + 1 }, () => []);
  for (let i=0; i<M; i++) {
    const [a, b] = input[line++].split(" ").map(Number);
    graph[a].push(b);
    graph[b].push(a);
  }

  const visited = Array.from({ length: N + 1 }, () => false);
  const dfs = (v) => {
    for (let w of graph[v]) {
      if (visited[w]) continue;
      visited[w] = true;
      dfs(w);
    }
  }

  let answer = 0;
  for (let i=1; i<N+1; i++) {
    if (visited[i]) continue;
    visited[i] = true;
    answer++;
    dfs(i);
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
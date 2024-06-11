/**
 * 제목 : 키 순서
 * 난이도 : 골드 4
 * 분류 : dfs, 단방향-그래프
 */

/**
 * 접근 방식
 * 1. 각각의 노드를 시작점으로 모든 노드를 dfs 순회 (bfs가 살짝 느렸음)
 * 2. visited[시작 노드][방문 노드], visited[방문 노드][시작 노드] 기록
 * 3. visited[노드]의 true(방문) 개수가 N - 1개 이면 answer에 카운트
 * 4. 플로이드 워셜로 바꿔서 풀어보니 소요시간이 더 오래 걸림
 * 
 * 개선
 * 1. smaller, bigger 배열 생성
 * 2. 단방향 그래프를 각 노드를 시작점으로 dfs 순회
 * 3. 순회하며 smaller와 depth 카운트
 * 4. bigger = depth - 1;
 * 5. answer 조건 smaller[node] + bigger[node] === N - 1
 */

const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [[N, _], edges] = [
    convertToNumArr(input[0]),
    input.slice(1).map(convertToNumArr),
  ];

  const graph = Array.from({ length: N }, () => []);
  for (const [a, b] of edges) graph[a - 1].push(b - 1);
  const smaller = Array.from({ length: N }, () => 0);
  const bigger = Array.from({ length: N }, () => 0);

  let visited, depth;

  const dfs = (s, v) => {
    depth++;
    for (const w of graph[v]) {
      if (visited[w]) continue;
      visited[w] = true;
      smaller[w]++;
      dfs(s, w);
    }
  };

  for (let i = 0; i < N; i++) {
    visited = Array.from({ length: N }, () => false);
    depth = 0;
    dfs(i, i);
    bigger[i] = depth - 1;
  }

  let answer = 0;
  for (let i = 0; i < N; i++) {
    if (smaller[i] + bigger[i] === N - 1) answer++;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
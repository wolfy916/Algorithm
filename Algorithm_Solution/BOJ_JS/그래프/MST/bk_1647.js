/**
 * 제목 : 도시분할 계획 - 백준(골드 4)
 * 분류 : MST, 그래프 이론
 */

/**
 * 접근 방식
 * 1. 노드 N개, 양방향 간선 M개, 가중치 C
 * 2. 간선 중심의 크루스칼 + union/find
 */

const solution = (input) => {
  let line = 0;
  const [N, M] = input[line++].split(" ").map(v => Number(v));
  let edges = [];
  while (line < M + 1) {
    edges.push(input[line++].split(" ").map(v => Number(v)));
  }

  edges.sort((a, b) => a[2] - b[2]);
  let par = Array.from({ length: N + 1 }, (_, i) => i);
  let [cnt, answer] = [0, 0];
  for (let [a, b, c] of edges) {
    if (cnt >= N - 2) break;
    if (find(a) != find(b)) {
      union(a, b);
      cnt += 1;
      answer += c;
    }
  }

  return answer;

  function find(x) {
    while (x != par[x]) {
      x = par[par[x]];
    }
    return x;
  };

  function union(x, y) {
    x = find(x, par);
    y = find(y, par);
    par[Math.min(x, y)] = Math.max(x, y);
  }
};

const input = require('fs').readFileSync('./input.txt').toString().split('\n');
console.log(solution(input));
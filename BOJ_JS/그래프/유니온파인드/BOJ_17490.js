/**
 * 제목 : 일감호에 다리 놓기
 * 난이도 : 골드 3
 * 분류 : 그래프, 그리디, 분리 집합, MST, 유니온-파인드
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const [N, M, K] = convert(input[0]);
  if (M <= 1) return "YES";
  if (K === 0) return "NO";
  const S = convert(input[1]);
  const visited = Array(N + 1).fill(false);
  const A = Array.from(Array(N + 1), (_, i) => [i - 1, i + 1]);
  A[1][0] = N;
  A[N][1] = 1;

  for (let i = 2; i < M + 2; i++) {
    const [a, b] = convert(input[i]).sort((a, b) => a - b);
    if (a === 1 && b === N) {
      A[a][0] = null;
      A[b][1] = null;
    } else {
      A[a][1] = null;
      A[b][0] = null;
    }
  }

  let answer = "YES";
  let sumV = 0;
  for (let i = 1; i < N + 1; i++) {
    if (visited[i]) continue;
    sumV += bfs(i);
    if (sumV <= K) continue;
    answer = "NO";
    break;
  }

  return answer;

  function bfs(s) {
    const queue = [s];
    visited[s] = true;
    let v, minV = Infinity;
    while (queue.length > 0) {
      v = queue.shift();
      minV = Math.min(minV, S[v - 1]);
      for (let i = 0; i < 2; i++) {
        if (A[v][i] === null || visited[A[v][i]]) continue;
        visited[A[v][i]] = true;
        queue.push(A[v][i]);
      }
    }
    return minV;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
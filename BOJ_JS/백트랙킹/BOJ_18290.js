/**
 * 제목 : NM과 K (1)
 * 난이도 : 실버 1
 * 분류 : 백트랙킹
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M, K] = convert(input.shift());
  const visited = Array.from(Array(N), () => Array(M).fill(0));
  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];
  for (let i = 0; i < N; i++) input[i] = convert(input[i]);

  let answer = -Infinity;
  search(0, 0, 0, 0);

  return answer;

  function check(i, j, b) {
    visited[i][j] += b;

    let ni, nj;
    for (let k = 0; k < 4; k++) {
      ni = i + di[k];
      nj = j + dj[k];
      if (ni < 0 || nj < 0 || ni >= N || nj >= M) continue;
      visited[ni][nj] += b;
    }
  }

  function search(vi, vj, count, value) {
    if (count === K) {
      answer = Math.max(answer, value);
      return;
    }

    for (let j = vj; j < M; j++) {
      if (visited[vi][j]) continue;
      check(vi, j, 1);
      search(vi, j + 1, count + 1, value + input[vi][j]);
      check(vi, j, -1);
    }

    for (let i = vi + 1; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (visited[i][j]) continue;
        check(i, j, 1);
        search(i, j + 1, count + 1, value + input[i][j]);
        check(i, j, -1);
      }
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 버섯 농장
 * 난이도 : 실버 1
 * 분류 : DFS
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M, K] = convert(input.shift());
  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];

  for (let i = 0; i < N; i++) {
    input[i] = convert(input[i]);
  }

  let cnt, remain = M;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (input[i][j]) continue;
      input[i][j] = 1;
      cnt = countPossible(i, j);
      remain -= Math.ceil(cnt / K);
      if (remain < 0) return "IMPOSSIBLE";
    }
  }

  if (remain === M) return "IMPOSSIBLE";

  return `POSSIBLE\n${remain}`;

  function countPossible(vi, vj) {
    let cnt = 1;

    for (let k = 0; k < 4; k++) {
      const ni = vi + di[k];
      const nj = vj + dj[k];
      if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
      if (input[ni][nj]) continue;
      input[ni][nj] = 1;
      cnt += countPossible(ni, nj);
    }

    return cnt;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
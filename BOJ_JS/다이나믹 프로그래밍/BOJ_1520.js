/**
 * 제목 : 내리막 길
 * 난이도 : 골드 3
 * 분류 : 다이나믹 프로그래밍 + DFS
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M] = convert(input.shift());
  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];
  const dp = Array.from(Array(N), () => Array(M).fill(-1));

  for (let i = 0; i < N; i++) {
    input[i] = convert(input[i]);
  }

  return count(0, 0);

  function isValid(i, j) {
    return i < 0 || j < 0 || i >= N || j >= M ? false : true;
  }

  function count(vi, vj) {
    if (vi === N - 1 && vj === M - 1) return 1;
    if (dp[vi][vj] >= 0) return dp[vi][vj];

    let countV = 0;

    for (let k = 0; k < 4; k++) {
      const ni = vi + di[k];
      const nj = vj + dj[k];
      if (!isValid(ni, nj)) continue;
      if (input[ni][nj] >= input[vi][vj]) continue;
      countV += count(ni, nj);
    }

    dp[vi][vj] = countV;

    return countV;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
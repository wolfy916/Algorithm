/**
 * 제목 : 욕심쟁이 판다
 * 난이도 : 골드 3
 * 분류 : 다이나믹 프로그래밍 + DFS
 */

const solution = (bamboo) => {
  const convert = (s) => s.split(" ").map(Number);
  const N = Number(bamboo.shift());
  const dp = Array.from(Array(N), () => Array(N).fill(0));
  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];

  for (let i = 0; i < N; i++) {
    bamboo[i] = convert(bamboo[i]);
  }

  let answer = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      answer = Math.max(answer, dfs(i, j) + 1);
    }
  }

  return answer;

  function isValid(i, j) {
    return i < 0 || j < 0 || i >= N || j >= N ? false : true;
  }

  function dfs(vi, vj) {
    if (dp[vi][vj]) return dp[vi][vj];

    let result = 0;

    for (let k = 0; k < 4; k++) {
      const ni = vi + di[k];
      const nj = vj + dj[k];
      if (!isValid(ni, nj)) continue;
      if (bamboo[vi][vj] >= bamboo[ni][nj]) continue;
      result = Math.max(result, dfs(ni, nj) + 1);
    }

    dp[vi][vj] = result;

    return result;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
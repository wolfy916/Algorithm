/**
 * 제목 : 합분해 2
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const [N, K] = input[0].split(" ").map(Number);
  const MOD = 1e9;
  const dp = Array.from(Array(N + 1), () => Array(K + 1).fill(0));

  for (let n = 1; n < N + 1; n++) dp[n][1] = 1;

  for (let k = 1; k < K + 1; k++) dp[0][k] = 1;

  for (let k = 2; k < K + 1; k++) {
    for (let n = 1; n < N + 1; n++) {
      dp[n][k] = (dp[n - 1][k] + dp[n][k - 1]) % MOD;
    }
  }

  return dp[N][K];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
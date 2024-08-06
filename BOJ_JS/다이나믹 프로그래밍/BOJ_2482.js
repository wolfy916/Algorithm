/**
 * 제목 : 색상환
 * 난이도 : 골드 3
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input[0]);
  const K = Number(input[1]);
  const MOD = 1e9 + 3;
  const dp = Array.from(Array(N + 1), () => new Array(K + 1).fill(0));

  for (let i=1; i<N + 1; i++) {
    dp[i][1] = i;
  }

  for (let n=4; n<N + 1; n++) {
    for (let k=2; k<K + 1; k++) {
      dp[n][k] = (dp[n - 1][k] + dp[n - 2][k - 1]) % MOD;
    }
  }

  return dp[N][K];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split('\n');
console.log(solution(input));
/**
 * 제목 : 삼각 그래프
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (N, input) => {
  const dp = input.map(v => v.split(" ").map(Number));
  dp[0][2] += dp[0][1];

  dp[1][0] += dp[0][1];
  dp[1][1] += Math.min(dp[1][0], dp[0][1], dp[0][2]);
  dp[1][2] += Math.min(dp[1][1], dp[0][1], dp[0][2]);

  for (let i=2; i<N; i++) {
    dp[i][0] += Math.min(dp[i - 1][0], dp[i - 1][1]);
    dp[i][1] += Math.min(dp[i][0], ...dp[i - 1]);
    dp[i][2] += Math.min(dp[i][1], dp[i - 1][1], dp[i - 1][2]);
  }

  return Math.min(dp[N - 1][1]);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let k = 1;
let idx = 0;
let N = Number(input[idx]);
while (N !== 0) {
  console.log(k++ + ". " + solution(N, input.slice(idx + 1, idx + N + 1)));
  idx += N + 1;
  N = Number(input[idx]);
}
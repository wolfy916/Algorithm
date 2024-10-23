/**
 * 제목 : 1학년
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input[0]);
  const arr = input[1].split(" ").map(Number);
  const dp = Array.from(Array(N - 1), () => Array(21).fill(0n));

  dp[0][arr[0]] = 1n;

  for (let i = 1; i < N - 1; i++) {
    for (let j = 0; j < 21; j++) {
      if (dp[i - 1][j] > 0n) {
        if (0 <= j + arr[i] && j + arr[i] < 21) {
          dp[i][j + arr[i]] += dp[i - 1][j];
        }

        if (0 <= j - arr[i] && j - arr[i] < 21) {
          dp[i][j - arr[i]] += dp[i - 1][j];
        }
      }
    }
  }

  return dp[N - 2][arr[N - 1]].toString();
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
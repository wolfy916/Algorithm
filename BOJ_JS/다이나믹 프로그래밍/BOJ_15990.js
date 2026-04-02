/**
 * 제목 : 1, 2, 3 더하기 5
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const T = Number(input[0]);
  const nums = Array.from({ length: T }, (_, i) => Number(input[i + 1]));

  const MOD = 1_000_000_009;
  const MAX_SIZE = 100_000;

  const dp = Array.from({ length: MAX_SIZE + 1 }, () => Array(3).fill(0));

  dp[1][0] = 1;
  dp[2][1] = 1;
  dp[3][0] = 1;
  dp[3][1] = 1;
  dp[3][2] = 1;

  for (let i = 4; i < MAX_SIZE + 1; i++) {
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD;
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % MOD;
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % MOD;
  }

  const answer = nums.map((v) => {
    return dp[v].reduce((a, c) => {
      return (a + c) % MOD;
    }, 0);
  });

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
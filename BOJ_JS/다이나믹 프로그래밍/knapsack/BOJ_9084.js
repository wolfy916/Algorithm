/**
 * 제목 : 동전
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍, 배낭 문제
 */

const solution = (input) => {
  const answer = [];
  let T = Number(input[0]);
  let idx = 1;

  while (T--) {
    const N = Number(input[idx++]);
    const coins = input[idx++].split(" ").map(Number);
    const M = Number(input[idx++]);
    const dp = Array(M + 1).fill(0);

    dp[0] = 1;

    for (const coin of coins) {
      for (let i = 1; i < M + 1; i++) {
        if (i < coin) continue;
        dp[i] += dp[i - coin];
      }
    }

    answer.push(dp[M]);
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
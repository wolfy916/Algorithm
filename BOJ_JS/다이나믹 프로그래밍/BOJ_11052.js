/**
 * 제목 : 카드 구매하기
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input[0]);
  const prices = input[1].split(" ").map(Number);

  const dp = Array.from({ length: N }, (_, i) => prices[i]);
  for (let i = 1; i < N; i++) {
    for (let j = 0; j < i; j++) {
      dp[i] = Math.max(dp[i], dp[i - j - 1] + prices[j]);
    }
  }

  return dp[N - 1];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
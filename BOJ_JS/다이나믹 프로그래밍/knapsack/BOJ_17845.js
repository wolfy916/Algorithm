/**
 * 제목 : 수강 과목
 * 난이도 : 골드 5
 * 분류 : knapsack(배낭 문제)
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, _] = convert(input[0]);
  const info = input.slice(1).map(convert);
  const dp = Array.from({ length: N + 1 }, () => 0);

  for (const [I, T] of info) {
    for (let i = N; i >= T; i--) {
      dp[i] = Math.max(dp[i], dp[i - T] + I);
    }
  }

  return dp[N];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 피보나치 함수
 * 난이도 : 실버 3
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const [T, ...nums] = input.map(Number);
  const maxSize = Math.max(...nums);

  if (maxSize === 0) return "1 0";

  const dp = Array.from(Array(maxSize + 1), () => [0, 0]);
  dp[0][0] = 1;
  dp[1][1] = 1;

  for (let i = 2; i < maxSize + 1; i++) {
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0];
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1];
  }

  const answer = [];
  for (let i = 0; i < T; i++) {
    answer.push(dp[nums[i]].join(" "));
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
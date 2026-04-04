/**
 * 제목 : 앱
 * 난이도 : 골드 3
 * 분류 : 다이나믹 프로그래밍, 배낭 문제
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);

  const [N, M] = convert(input[0]);
  const memories = convert(input[1]);
  const costs = convert(input[2]);

  const TOTAL_COST = costs.reduce((a, c) => a + c, 0);
  const dp = Array.from({ length: TOTAL_COST + 1 }, () => 0);

  for (let i = 0; i < N; i++) {
    const currentMemory = memories[i];
    const currentCost = costs[i];

    for (let cost = TOTAL_COST; cost >= currentCost; cost--) {
      dp[cost] = Math.max(dp[cost - currentCost] + currentMemory, dp[cost]);
    }
  }

  const answer = dp.findIndex((v) => v >= M);

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 호텔
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍, 배낭 문제
 */

// 2차원 풀이를 1차원으로 해결할 수 있을지 고민해볼 것!

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [C, N] = convert(input[0]);
  const dp = Array(C + 101).fill(Infinity);

  dp[0] = 0;

  for (let i = 1; i < N + 1; i++) {
    const [c, n] = convert(input[i]);
    for (let j = n; j < C + 101; j++) {
      dp[j] = Math.min(dp[j - n] + c, dp[j]);
    }
  }

  return Math.min(...dp.slice(C,));
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 파이프 옮기기 1
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍, 누적합
 */

const solution = (input) => {
  const N = Number(input[0]);
  const house = input.slice(1).map((v) => v.split(" ").map(Number));
  const dp = Array.from(Array(N), () => {
    return Array.from(Array(N), () => [0, 0, 0]);
  });

  for (let j = 1; j < N; j++) {
    if (house[0][j] === 1) break;
    dp[0][j][0] = 1;
  }

  for (let i = 1; i < N; i++) {
    for (let j = 1; j < N; j++) {
      if (house[i][j] === 1) continue;
      dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2];
      dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2];
      if (house[i][j - 1] || house[i - 1][j] || house[i - 1][j - 1]) continue;
      dp[i][j][2] = dp[i - 1][j - 1].reduce((a, c) => a + c);
    }
  }

  return dp[N - 1][N - 1].reduce((a, c) => a + c);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
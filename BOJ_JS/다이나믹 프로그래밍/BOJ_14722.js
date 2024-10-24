/**
 * 제목 : 우유 도시
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input.shift());
  const board = input.map((v) => v.split(" ").map(Number));
  const dp = Array.from(Array(N + 1), () => Array(N + 1).fill(0));

  for (let i = 1; i < N + 1; i++) {
    for (let j = 1; j < N + 1; j++) {
      dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      if (dp[i][j] % 3 !== board[i - 1][j - 1]) continue;
      dp[i][j] += 1;
    }
  }

  return dp[N][N];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
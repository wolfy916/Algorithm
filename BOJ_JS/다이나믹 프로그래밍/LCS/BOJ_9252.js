/**
 * 제목 : LCS 2
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍, LCS(최장 공통 부분 수열)
 */

const solution = (input) => {
  const s1 = input[0].trim();
  const s2 = input[1].trim();
  const [N, M] = [s1.length, s2.length];
  const dp = Array.from(Array(N + 1), () => Array(M + 1).fill(""));

  for (let i = 1; i < N + 1; i++) {
    for (let j = 1; j < M + 1; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + s1[i - 1];
      } else {
        if (dp[i][j - 1].length <= dp[i - 1][j].length) {
          dp[i][j] = dp[i - 1][j];
        } else {
          dp[i][j] = dp[i][j - 1];
        }
      }
    }
  }

  return dp[N][M].length + "\n" + dp[N][M];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
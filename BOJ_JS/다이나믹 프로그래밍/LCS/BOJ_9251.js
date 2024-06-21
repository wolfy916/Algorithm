/**
 * 제목 : LCS
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍, LCS;
 */

const solution = (input) => {
  const str1 = input[0].trim();
  const str2 = input[1].trim();
  const [N, M] = [str1.length, str2.length];

  const dp = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: M + 1 }, () => 0);
  });

  for (let i = 1; i < N + 1; i++) {
    for (let j = 1; j < M + 1; j++) {
      if (str1[i - 1] === str2[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
      else dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
    }
  }

  return dp[N][M];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
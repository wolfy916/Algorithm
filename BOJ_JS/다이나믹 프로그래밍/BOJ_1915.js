/**
 * 제목 : 가장 큰 정사각형
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍
 */

const convert = (strArr) => strArr.trim().split("").map(Number);

const solution = (input) => {
  const [N, M] = input[0].split(" ").map(Number);
  const dp = input.slice(1).map(convert);
  let answer = 0;

  for (let i = 1; i < N; i++) {
    for (let j = 1; j < M; j++) {
      if (dp[i][j] > 0) {
        dp[i][j] += Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      answer = Math.max(answer, dp[i][j]);
    }
  }

  return Math.pow(answer, 2);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
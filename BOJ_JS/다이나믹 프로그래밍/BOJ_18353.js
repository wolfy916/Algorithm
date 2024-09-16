/**
 * 제목 : 병사 배치하기
 * 난이도 : 실버 2
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input[0]);
  const num = input[1].split(" ").map(Number);
  const dp = Array(N).fill(1);

  for (let i = 0; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {
      if (num[i] > num[j]) {
        dp[j] = Math.max(dp[j], dp[i] + 1);
      }
    }
  }

  return N - Math.max(...dp);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

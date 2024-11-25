/**
 * 제목 : 가장 긴 바이토닉 부분 수열
 * 난이도 : 골드 4
 * 분류 : LIS
 */

const solution = (input) => {
  const N = Number(input[0]);
  const A = input[1].split(" ").map(Number);
  const dp = Array.from(Array(N), () => [1, 1]);

  for (let i=1; i<N; i++) {
    for (let j=0; j < i; j++) {
      if (A[i] <= A[j]) continue;
      dp[i][0] = Math.max(dp[i][0], dp[j][0] + 1);
    }
  }

  for (let i=N - 2; i>=0; i--) {
    for (let j=i + 1; j < N; j++) {
      if (A[i] <= A[j]) continue;
      dp[i][1] = Math.max(dp[i][1], dp[j][1] + 1);
    }
  }

  return Math.max(...dp.map(v => v[0] + v[1])) - 1;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
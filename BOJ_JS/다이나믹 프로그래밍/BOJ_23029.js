/**
 * 제목 : 시식 코너는 나의 것
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const [N, foods] = [Number(input[0]), input.slice(1,).map(Number)];
  
  const dp = Array.from({ length: N }, () => [0, 0, 0]);

  dp[0][1] = foods[0];

  for (let i=1; i<N; i++) {
    dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1], dp[i-1][2]);
    dp[i][1] = foods[i] + dp[i-1][0];
    dp[i][2] = Math.floor(foods[i] / 2) + dp[i-1][1];
  }

  return Math.max(...dp[N-1]);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
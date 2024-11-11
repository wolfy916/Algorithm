/**
 * 제목 : 제곱수의 합
 * 난이도 : 실버 2
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input[0]);
  const dp = Array(N + 1).fill(0);

  let minV, square;
  for (let i = 1; i < N + 1; i++) {
    minV = Infinity;
    for (let j = 1; j < Math.floor(Math.sqrt(i)) + 1; j++) {
      square = Math.pow(j, 2);
      minV = Math.min(minV, dp[i - square] + 1);
    }
    dp[i] = minV;
  }

  return dp[N];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
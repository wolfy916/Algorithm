/**
 * 제목 : 극장 좌석
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍(피보나치)
 */

const solution = (input) => {
  const N = Number(input[0]);
  const M = Number(input[1]);
  if (N === M) return 1;
  const seats = input.slice(2,).map(Number);
  const dp = Array(N + 1).fill(0);

  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 2;
  
  for (let i=3; i<N + 1; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  
  let answer = 1;
  let prev = 0;

  for (const seat of seats) {
    answer *= dp[seat - prev - 1];
    prev = seat;
  }

  answer *= dp[N - prev];

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
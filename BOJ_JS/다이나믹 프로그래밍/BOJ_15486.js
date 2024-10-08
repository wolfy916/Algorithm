/**
 * 제목 : 퇴사 2
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input[0]);
  const info = input.slice(1,).map(v => v.split(" ").map(Number));
  const dp = Array(N + 1).fill(0);
  
  let tmp;
  for (let i=1; i<N + 1; i++) {
    dp[i] = Math.max(dp[i], dp[i - 1]);
    tmp = i + info[i - 1][0] - 1
    if (tmp > N) continue;
    dp[tmp] = Math.max(dp[tmp], dp[i - 1] + info[i - 1][1]);
  }

  return Math.max(...dp);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
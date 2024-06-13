/**
 * 제목 : 오르막 수
 * 난이도 : 실버 1 
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input);
  const dp = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: 10 }, () => 0);
  });

  for (let i=0; i<10; i++) dp[1][i] = 1;

  for (let i=2; i<N+1; i++) {
    dp[i][0] = dp[i-1][0] % 10007;
    for (let num=1; num<10; num++) {
      dp[i][num] = (dp[i][num - 1] + dp[i - 1][num]) % 10007;
    }
  }

  return dp[N].reduce((acc, cur) => acc + cur, 0) % 10007;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
for (const line of inputArr) {
  console.log(solution(line));
}
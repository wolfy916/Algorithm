/**
 * 제목 : 1, 2, 3 더하기 6
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const T = Number(input[0]);
  const dp = Array.from({ length: 1e5 + 1 }, () => 0);
  const answer = [];
  const INF = 1e9 + 9;

  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 2;
  dp[4] = 3;
  dp[5] = 3;
  dp[6] = 6;

  for (let i=7; i<1e5 + 1; i++) {
    dp[i] = (dp[i] + dp[i - 2]) % INF;
    dp[i] = (dp[i] + dp[i - 4]) % INF;
    dp[i] = (dp[i] + dp[i - 6]) % INF;
  }

  for (let t=1; t<T + 1; t++) {
    const num = Number(input[t]);
    answer.push(dp[num]);
  }

  return answer.join('\n');
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
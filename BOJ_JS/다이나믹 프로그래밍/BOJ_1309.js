/**
 * 제목 : 동물원
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = +input;
  const dp = [[1, 1], [0, 0]];

  let [cur, iter] = [0, 0];
  while (iter++ < N) {
    nxt = (cur + 1) % 2;
    dp[nxt][0] = (dp[cur][0] + dp[cur][1] * 2) % 9901;
    dp[nxt][1] = (dp[cur][0] + dp[cur][1]) % 9901;
    cur = nxt;
  }

  return dp[cur][0];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim();
console.log(solution(inputArr));
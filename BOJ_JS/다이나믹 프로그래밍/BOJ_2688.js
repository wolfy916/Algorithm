/**
 * 제목 : 줄어들지 않아
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const nums = input.slice(1,).map(Number);
  const len = Math.max(...nums);
  const dp = Array.from({ length: len }, () => {
    return Array.from({ length: 10 }, () => 0);
  });
  const sumArr = Array.from({ length: len }, () => 0);
  
  for (let i=0; i<10; i++) dp[0][i] = 1;
  sumArr[0] = 10;
  
  for (let i=1; i<len; i++) {
    sumArr[i] += sumArr[i - 1];
    dp[i][0] = sumArr[i - 1];
    for (let j=1; j<10; j++) {
      dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1];
      sumArr[i] += dp[i][j];
    }
  }

  return nums.map(v => sumArr[v - 1]).join('\n');
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
/**
 * 제목 : 결전의 금요일
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const nums = input[1].split(" ").map(Number);
  
  let dp = Array(7).fill(false);
  dp[0] = true;

  for (const num of nums) {
    const tmp = Array(7).fill(false);
    for (let i=0; i<7; i++) {
      if (!dp[i]) continue;
      tmp[(i + num) % 7] = true;
      tmp[i] = true;
    }
    dp = tmp;
  }
  
  return dp[4] ? "YES" : "NO";
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
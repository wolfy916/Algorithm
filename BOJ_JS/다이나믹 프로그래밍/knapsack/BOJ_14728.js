/**
 * 제목 : 벼락치기
 * 난이도 : 골드5
 * 분류 : 냅색
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, T] = convert(input[0]);
  const info = input.slice(1).map(convert);

  const dp = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: T + 1 }, () => 0);
  });

  for (let i = 1; i < N + 1; i++) {
    const [K, S] = info[i - 1];
    for (let j = 1; j < T + 1; j++) {
      if (j >= K) {
        dp[i][j] = Math.max(dp[i - 1][j], S + dp[i - 1][j - K]);
      } else {
        dp[i][j] = dp[i - 1][j];
      }
    }
  }
  
  return dp[N][T];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
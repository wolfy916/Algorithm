/**
 * 제목 : 합분해
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (N, K) => {
  const dp = Array.from({ length: N + 1 }, () => {
    return Array.from({ length : K + 1 }, () => 0);
  });

  for (let i=0; i<N + 1; i++) {
    dp[i][1] = 1;
  }
  
  return getDP(N, K);

  function getDP(n, k) {
    if (dp[n][k] > 0) return dp[n][k];
    
    let sumV = 0;
    for (let i=0; i<n + 1; i++) {
      sumV += getDP(i, k - 1);
    }

    dp[n][k] += sumV;
    dp[n][k] %= 1e9;

    return dp[n][k];
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);
console.log(solution(...input));
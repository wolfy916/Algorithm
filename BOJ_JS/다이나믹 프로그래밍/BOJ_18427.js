/**
 * 제목 : 함께 블록 쌓기
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, M, H] = convert(input[0]);
  const MOD = 10007;

  const dp = Array.from(Array(N + 1), () => {
    return Array.from(Array(H + 1), () => 0);
  });

  dp[0][0] = 1;

  for (let i=1; i<N + 1; i++) {
    const heights = convert(input[i]);

    for (let j=0; j<H + 1; j++) {
      dp[i][j] += dp[i - 1][j];
    }

    for (const h of heights) {
      for (let j=h; j < H+1; j++) {
        dp[i][j] += dp[i - 1][j - h];
        dp[i][j] %= MOD;
      }
    }
  }
  
  return dp[N][H];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 암호코드
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const password = input;
  const len = password.length;
  const dp = Array.from(Array(len + 1), () => new Array(2).fill(0));
  const MOD = 1e6;

  if (password[0] !== '0') {
    dp[1][0] = 1;
    const tmp = convert(0, 2);
    if (1 <= tmp && tmp <= 26) {
      dp[1][1] = 1;
    }
  }

  for (let i=2; i<len + 1; i++) {
    if (password[i - 1] === '0') continue;
    dp[i][0] = (dp[i - 1][0] + dp[i - 2][1]) % MOD;
    if (i >= len) continue;
    const num = convert(i - 1, i + 1);
    if (1 > num || num > 26) continue;
    dp[i][1] = (dp[i - 1][0] + dp[i - 2][1]) % MOD;
  }

  return (dp[password.length][0] + dp[password.length - 1][1]) % MOD;

  function convert(i, j) {
    return Number(password.slice(i, j));
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();
console.log(solution(input));
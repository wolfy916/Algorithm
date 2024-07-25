/**
 * 제목 : 하노이 탑
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input);
  if (N === 1) return "1\n1 3";
  const dp = Array.from({ length: N + 1 }, () => 0);
  const log = [];

  dp[1] = 1;
  for (let i = 2; i < N + 1; i++) {
    dp[i] = BigInt(dp[i - 1]) * BigInt(2) + BigInt(1);
  }

  if (N <= 20) hanoi(N, 1, 2, 3);

  return dp[N] + "\n" + log.join("\n");

  function hanoi(n, start, temp, target) {
    if (n === 0) return;
    hanoi(n - 1, start, target, temp);
    log.push(start + " " + target);
    hanoi(n - 1, temp, start, target);
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();
console.log(solution(input));
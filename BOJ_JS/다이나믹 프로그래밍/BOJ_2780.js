/**
 * 제목 : 비밀번호
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const T = Number(input[0]);
  const passwordLengths = Array.from({ length: T }, (_, i) =>
    Number(input[i + 1]),
  );

  const MOD = 1_234_567;
  const MAX_LENGTH = Math.max(...passwordLengths);
  const availableNumbers = [
    [7],
    [2, 4],
    [1, 3, 5],
    [2, 6],
    [1, 5, 7],
    [2, 4, 6, 8],
    [3, 5, 9],
    [0, 4, 8],
    [5, 7, 9],
    [6, 8],
  ];

  const dp = Array.from({ length: MAX_LENGTH + 1 }, () => Array(10).fill(0));

  for (let i = 0; i < 10; i++) {
    dp[1][i] = 1;
  }

  for (let length = 2; length < MAX_LENGTH + 1; length++) {
    for (let number = 0; number < 10; number++) {
      for (const aN of availableNumbers[number]) {
        dp[length][number] += dp[length - 1][aN];
        dp[length][number] %= MOD;
      }
    }
  }

  const answer = [];

  for (const pL of passwordLengths) {
    const value = dp[pL].reduce((a, c) => (a + c) % MOD);
    answer.push(value);
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 그림 교환
 * 난이도 : 골드 1
 * 분류 : 다이나믹 프로그래밍, 비트마스킹
 */

const solution = (input) => {
  const N = Number(input[0]);
  const prices = Array.from({ length: N }, (_, i) => {
    return input[i + 1].split("").map(Number);
  });

  const dp = Array.from({ length: 1 << N }, () => {
    return Array.from({ length: N }, () => {
      return Array(10).fill(-1);
    });
  });

  const countBits = (mask) => {
    let cnt = 0;

    while (mask) {
      mask &= mask - 1;
      cnt++;
    }

    return cnt;
  };

  const dfs = (visited, last, price) => {
    if (dp[visited][last][price] > -1) {
      return dp[visited][last][price];
    }

    let result = countBits(visited);

    for (let i = 0; i < N; i++) {
      if (visited & (1 << i)) continue;
      if (prices[last][i] < price) continue;

      result = Math.max(result, dfs(visited | (1 << i), i, prices[last][i]));
    }

    return (dp[visited][last][price] = result);
  };

  const answer = dfs(1 << 0, 0, 0);

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

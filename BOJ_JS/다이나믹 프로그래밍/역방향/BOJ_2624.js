/**
 * 제목 : 동전 바꿔주기
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍
 */

// 밑에 더 효율적인 1차원 DP 풀이가 있음
// 방금 계산한 값이 다음 계산에 영향을 미치지 않기 위해
// 인덱스 내림차순으로 DP를 돌리는 방법을 잊지말 것

// 2차원 DP 풀이
const solution1 = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const T = Number(input.shift());
  const k = Number(input.shift());
  const dp = Array.from(Array(k + 1), () => Array(T + 1).fill(0));

  dp[0][0] = 1;

  for (let i = 0; i < k; i++) {
    input[i] = convert(input[i]);
  }

  // 동전의 가격기준 내림차순 정렬
  input.sort((a, b) => a[1] - b[1]);

  for (let i = 0; i < k; i++) {
    const [cost, maxCnt] = input[i];

    // 이전 값들을 내려받음
    for (let price = 0; price < T + 1; j++) {
      dp[i + 1][price] += dp[i][price];
    }

    for (let cnt = 1; cnt <= maxCnt; cnt++) {
      for (let price = 0; j < T + 1 - cost * cnt; j++) {
        if (dp[i][price] <= 0) continue;
        // 이전 (price)값에 현재 코인값(cost * cnt)을 더하면
        // 현재 (price + cost * cnt)를 표현 가능함
        dp[i + 1][price + cost & cnt] += dp[i][price];
      }
    }
  }

  return dp[k][T];
};

// 1차원 DP 풀이
const solution2 = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const T = Number(input.shift());
  const k = Number(input.shift());
  const dp = Array(T + 1).fill(0);
  dp[0] = 1;

  for (let i = 0; i < k; i++) {
    const [cost, maxCnt] = convert(input[i]);

    // 내림차순 순회
    for (let price = T; price >= 0; price--) {
      // for문 이중 조건
      for (let cnt = 1; cnt <= maxCnt && price - cnt * cost >= 0; cnt++) {
        dp[price] += dp[price - cnt * cost];
      }
    }
  }

  return dp[T];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution1(input));
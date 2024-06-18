/**
 * 제목 : Ezreal 여눈부터 가네 ㅈㅈ
 * 난이도 : 골드 5
 * 분류 : 수학, 다이나믹 프로그래밍, 정수론
 */

/**
 * 접근 방식
 * 1. 각 자리수를 추가할 때마다, 현재 자리까지의 숫자의 합이 3의 배수인 경우의수를 카운트
 * 2. 마지막 자리가 5인 경우만 고려
 */

const solution = (input) => {
  const N = Number(input[0]);
  const mod = 1000000007;

  // DP 배열 초기화
  const dp = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: 3 }, () => 0);
  });
  
  // 초기 설정
  dp[1][0] = 0;
  dp[1][1] = 1;
  dp[1][2] = 1;

  for (let i = 2; i <= N; i++) {
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % mod;
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod;
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % mod;
  }
  
  return dp[N - 1][1];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
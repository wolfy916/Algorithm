/**
 * 제목 : 팰린드롬?
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  // 데이터 입력 및 초기화
  const N = Number(input[0]);
  const nums = convert(input[1]);
  const questions = input.slice(3,).map(convert);

  // dp[i][j] = i번째 수부터 j번째 까지 수의 팰린드롬 여부
  const dp = Array.from({ length: N }, () => {
    return Array.from({ length: N }, () => null);
  });

  // 원소 1개의 경우 => 무조건 팰린드롬
  for (let i=0; i<N; i++) {
    dp[i][i] = 1;
  }

  // 원소 2개의 경우 => 팰린드롬 여부 확인하여 처리
  for (let i=0; i<N - 1; i++) {
    dp[i][i + 1] = nums[i] === nums[i + 1] ? 1 : 0;
  }

  // 질문 처리
  const answer = [];
  for (const [i, j] of questions) {
    answer.push(getDP(i - 1, j - 1));
  }

  return answer.join('\n');

  // DP 값이 있으면 return 없으면 갱신
  function getDP(i, j) {
    if (dp[i][j] !== null) return dp[i][j];
    dp[i][j] = getDP(i + 1, j - 1) && nums[i] === nums[j] ? 1 : 0;
    return dp[i][j];
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
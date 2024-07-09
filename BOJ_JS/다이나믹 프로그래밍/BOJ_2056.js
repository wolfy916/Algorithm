/**
 * 제목 : 작업
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const N = Number(input[0]);
  const infos = input.slice(1).map(convert);
  const dp = Array.from({ length: N + 1 }, () => 0);
  let answer = 0;

  for (let i = 0; i < N; i++) {
    const [t, n, ...work] = infos[i];
    if (n < 1) {
      dp[i + 1] = t;
    } else {
      dp[i + 1] = t + Math.max(...work.map((v) => dp[v]));
    }
    answer = Math.max(answer, dp[i + 1]);
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 구간 나누기
 * 난이도 : 골드 3
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const [N, M] = input[0].split(" ").map(Number);
  const nums = input.slice(1).map(Number);

  const dp1 = Array.from({ length: N + 1 }, () => {
    return [0].concat(Array(M).fill(-Infinity));
  });
  const dp2 = Array.from({ length: N + 1 }, () => {
    return [0].concat(Array(M).fill(-Infinity));
  });

  for (let i = 1; i <= N; i++) {
    for (let j = 1; j <= Math.min(M, Math.ceil(i / 2)); j++) {
      dp1[i][j] = Math.max(dp1[i - 1][j], dp2[i - 1][j]);
      dp2[i][j] = Math.max(dp1[i - 1][j - 1], dp2[i - 1][j]) + nums[i - 1];
    }
  }

  return Math.max(dp1[N][M], dp2[N][M]);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 사과나무
 * 난이도 : 골드 5
 * 분류 : 누적합, 브루트포스
 */

const solution = (input) => {
  const N = Number(input[0]);
  const prefixSum = Array.from(Array(N + 1), () => Array(N + 1).fill(0));

  let line;
  for (let i = 1; i < N + 1; i++) {
    line = input[i].split(" ").map(Number);
    for (let j = 0; j < N; j++) {
      prefixSum[i][j + 1] = line[j];
    }
  }

  for (let i = 1; i < N + 1; i++) {
    for (let j = 1; j < N + 1; j++) {
      prefixSum[i][j] += prefixSum[i][j - 1];
    }
  }

  for (let j = 1; j < N + 1; j++) {
    for (let i = 1; i < N + 1; i++) {
      prefixSum[i][j] += prefixSum[i - 1][j];
    }
  }

  let answer = -Infinity;
  let size = 0;
  while (++size <= N) {
    for (let i = size; i < N + 1; i++) {
      for (let j = size; j < N + 1; j++) {
        answer = Math.max(answer, getValue(i, j, size));
      }
    }
  }

  return answer;

  function getValue(i, j, size) {
    return (
      prefixSum[i][j] - prefixSum[i - size][j] - prefixSum[i][j - size] + prefixSum[i - size][j - size]
    );
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
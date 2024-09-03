/**
 * 제목 : 두 배
 * 난이도 : 골드 4
 * 분류 : 수학, 그리디
 */

const solution = (input) => {
  const N = Number(input[0]);
  const A = input[1].split(" ").map(Number);
  const count = Array(N).fill(0);

  let answer = 0;
  for (let i = 1; i < N; i++) {
    count[i] = Math.max(Math.ceil(Math.log2(A[i - 1] / A[i])) + count[i - 1], 0);

    answer += count[i];
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 나무 자르기
 * 난이도 : 실버 2
 * 분류 : 그리디, 정렬
 */

const solution = (input) => {
  const n = Number(input[0]);
  const H = input[1].split(" ").map(Number);
  const A = input[2].split(" ").map(Number);
  const arr = Array.from(Array(n), () => [0, 0]);

  for (let i = 0; i < n; i++) {
    arr[i][0] = H[i];
    arr[i][1] = A[i];
  }

  arr.sort((a, b) => a[1] - b[1]);

  let answer = 0;

  for (let i = 0; i < n; i++) {
    answer += arr[i][0] + arr[i][1] * i;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
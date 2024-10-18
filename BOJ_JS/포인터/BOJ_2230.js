/**
 * 제목 : 수 고르기
 * 난이도 : 골드 5
 * 분류 : 투 포인터
 */

const solution = (input) => {
  const [N, M] = input.shift().split(" ").map(Number);
  const A = input.map(Number);

  A.sort((a, b) => a - b);

  let [p1, p2] = [0, 1];
  let answer = Infinity;
  let diff;
  while (p2 < N) {
    diff = A[p2] - A[p1];
    if (diff < M) {
      p2++;
    } else if (diff > M) {
      answer = Math.min(answer, diff);
      p1++;
    } else return diff;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
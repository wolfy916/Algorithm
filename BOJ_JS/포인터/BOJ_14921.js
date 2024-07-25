/**
 * 제목 : 용액 합성하기
 * 난이도 : 골드 5
 * 분류 : 투 포인터
 */

const solution = (input) => {
  const N = Number(input[0]);
  const A = input[1].split(" ").map(Number);

  A.sort((a, b) => a - b);

  let [p1, p2] = [0, N - 1];
  let answer = Infinity;
  let sumV;
  while (p1 < p2) {
    sumV = A[p1] + A[p2];
    if (Math.abs(answer) > Math.abs(sumV)) {
      answer = sumV;
    }
    if (sumV < 0) {
      p1++;
    } else if (sumV > 0) {
      p2--;
    } else break;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
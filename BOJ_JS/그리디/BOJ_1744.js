/**
 * 제목 : 수 묶기
 * 난이도 : 골드 4
 * 분류 : 그리디, 정렬, 많은 조건 분기
 */

const solution = (input) => {
  const N = Number(input[0]);
  const plus = [];
  const minus = [];
  let answer = 0;

  for (let i = 1; i < N + 1; i++) {
    const num = Number(input[i]);
    if (num > 1) plus.push(num);
    else if (num < 1) minus.push(num);
    else answer++;
  }

  plus.sort((a, b) => b - a);
  for (let i = 0; i < plus.length; i += 2) {
    if (i < plus.length - 1) {
      answer += plus[i] * plus[i + 1];
    } else {
      answer += plus[i];
    }
  }

  minus.sort((a, b) => a - b);
  for (let i = 0; i < minus.length; i += 2) {
    if (i < minus.length - 1) {
      answer += minus[i] * minus[i + 1];
    } else {
      answer += minus[i];
    }
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
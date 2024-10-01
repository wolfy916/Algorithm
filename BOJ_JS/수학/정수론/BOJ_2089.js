/**
 * 제목 : -2진수
 * 난이도 : 실버 2
 * 분류 : 수학, 정수론
 */

const solution = (input) => {
  let num = Number(input[0]);
  if (num === 0) return 0;
  let tmp;
  const answer = [];
  while (num !== 0) {
    tmp = Math.ceil(num / -2);
    answer.push(num - tmp * - 2);
    num = tmp;
  }
  return answer.reverse().join("");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
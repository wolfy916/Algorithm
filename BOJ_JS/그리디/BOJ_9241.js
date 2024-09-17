/**
 * 제목 : 바이러스 복제
 * 난이도 : 골드 5
 * 분류 : 문자열, 그리디
 */

const solution = (input) => {
  const DNA1 = input[0].trim();
  const DNA2 = input[1].trim();

  let start = 0;
  const minN = Math.min(DNA1.length, DNA2.length);
  while (start < minN) {
    if (DNA1[start] !== DNA2[start]) break;
    start++;
  }

  let end = 0;
  while (end < minN) {
    if (DNA1[DNA1.length - 1 - end] !== DNA2[DNA2.length - 1 - end]) break;
    end++;
  }

  let answer;
  if (start >= minN - end) {
    if (DNA1.length > DNA2.length) {
      answer = 0;
    } else {
      answer = DNA2.length - DNA1.length;
    }
  } else {
    answer = DNA2.length - end - start;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
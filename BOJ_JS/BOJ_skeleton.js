/**
 * 제목 : 
 * 난이도 : 
 * 분류 : 
 */

/**
 * 접근 방식
 * 
 */

const solution = (input) => {
  const answer = [];
  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
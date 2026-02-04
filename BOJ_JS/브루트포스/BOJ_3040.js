/**
 * 제목 : 백설 공주와 일곱 난쟁이
 * 난이도 : 브론즈 2
 * 분류 : 브루트 포스
 */

const solution = (input) => {
  const nums = input.map(Number);
  const answer = [];

  const backtracking = (idx = 0) => {
    const sumV = answer.reduce((ac, cur) => ac + cur, 0);
    if (sumV === 100 && answer.length === 7) return true;
    if (sumV > 100 || answer.length > 7 || idx > 8) return false;

    answer.push(nums[idx]);
    if (backtracking(idx + 1)) return true;
    answer.pop();
    return backtracking(idx + 1);
  };

  backtracking();

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

/**
 * 제목 : 순서쌍의 곱의 합
 * 난이도 : 실버 4
 * 분류 : 수학, 누적합
 */

const solution = (input) => {
  const n = Number(input[0]);
  const nums = input[1].split(" ").map(v => BigInt(v));

  let sumV = nums[0] + nums[1];
  let multipleV = nums[0] * nums[1];

  if (n < 3) return multipleV.toString();

  for (let i=2; i<n; i++) {
    multipleV += sumV * nums[i];
    sumV += nums[i];
  }

  return multipleV.toString();
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
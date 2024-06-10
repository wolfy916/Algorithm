/**
 * 제목 : 부분합
 * 난이도 : 골드4
 * 분류 : 투 포인터
 */

const solution = (input) => {
  const [N, S] = input[0].split(" ").map(Number);
  const nums = input[1].split(" ").map(Number);

  let [left, right] = [0, 0];
  let sumV = 0;
  let answer = 100000;
  while (left < N) {
    while (right < N && sumV < S) sumV += nums[right++];
    if (sumV >= S) answer = Math.min(answer, right - left);
    sumV -= nums[left++];
  }

  return answer < 100000 ? answer : 0;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
/**
 * 제목 : List of Unique Numbers
 * 난이도 : 골드4
 * 분류 : 투 포인터
 */


const solution = (input) => {
  const [N, nums] = [+input[0], input[1].split(" ").map(Number)];

  let answer = 0;
  let [p1, p2] = [0, 0];
  const set = new Set();
  while (p2 < N) {
    while (p2 < N && !set.has(nums[p2])) {
      set.add(nums[p2++]);
    }
    while (p1 < p2 && nums[p1] !== nums[p2]) {
      answer += p2 - p1;
      set.delete(nums[p1++]);
    }
    answer += p2 - p1;
    set.delete(nums[p1++]);
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
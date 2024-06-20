/**
 * 제목 : 세 번째
 * 난이도 : 실버 2
 * 분류 : 그리디
 */

const solution = (input) => {
  const arr = input.slice(1).map((v) => v.trim());

  arr.sort((a, b) => a - b);

  const nums = [];
  const used = Array.from({ length: 4 }, () => false);

  const dfs = (strArr) => {
    if (strArr.length === 2) {
      nums.push(strArr.join(""));
      return;
    }
    for (let i = 0; i < 4; i++) {
      if (used[i] || arr[i] === undefined) continue;
      used[i] = true;
      strArr.push(arr[i]);
      dfs(strArr);
      used[i] = false;
      strArr.pop();
    }
  };

  dfs([]);

  nums.sort((a, b) => a - b);

  return nums[2];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
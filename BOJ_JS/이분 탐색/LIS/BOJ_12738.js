/**
 * 제목 : 가장 긴 증가하는 부분 수열 3
 * 난이도 : 골드 2
 * 분류 : LIS, 이분탐색
 */

const solution = (input) => {
  const N = Number(input[0]);
  const nums = input[1].split(" ").map(Number);

  const binarySearch = (left, right, target) => {
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (target < LIS[mid]) {
        right = mid - 1;
      } else if (LIS[mid] < target) {
        left = mid + 1;
      } else return mid;
    }
    return left;
  }

  const LIS = [nums[0]];

  for (let i=1; i<N; i++) {
    if (LIS[LIS.length - 1] < nums[i]) {
      LIS.push(nums[i]);
    } else {
      LIS[binarySearch(0, LIS.length - 1, nums[i])] = nums[i];
    }
  }

  return LIS.length;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 가장 긴 증가하는 부분 수열
 * 난이도 : 실버 2
 * 분류 : LIS(최장 증가 부분 수열)
 */

/**
 * 접근 방식
 * 1. 이분 탐색을 적용한 LIS(DP보다 빠르당)
 * 2. 시간복잡도 : O(nlog n)
 */

const solution = (input) => {
  const [N, nums] = [
    +input[0],
    input[1].split(" ").map(v => +v),
  ];

  const LIS = [nums[0]];

  const binarySearch = (num) => {
    let [left, right] = [0, LIS.length - 1];
    let mid;
    while (left <= right) {
      mid = Math.floor((left + right) / 2);
      if (LIS[mid] >= num) {
        right = mid - 1;
      } else {
        left = mid + 1 ;
      }
    }
    return LIS[mid] < num ? mid + 1 : mid;
  }

  let idx;
  for (let i=1; i<N; i++) {
    idx = binarySearch(nums[i]);
    if (LIS.length <= idx) {
      LIS.push(nums[i]);
    } else {
      LIS[idx] = nums[i];
    }
  }

  return LIS.length;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
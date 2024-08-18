/**
 * 제목 : 배
 * 난이도 : 골드 5
 * 분류 : 그리디, 정렬
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const N = Number(input[0]);
  const cranes = convert(input[1]);
  const M = Number(input[2]);
  const boxes = convert(input[3]);

  cranes.sort((a, b) => a - b);
  boxes.sort((a, b) => a - b);

  if (cranes[N - 1] < boxes[M - 1]) return -1;

  const startIdxArr = Array(N).fill(-1);
  for (let i=0; i<N; i++) {
    startIdxArr[i] = BinarySearch(i);
  }

  let answer = 0;
  let restBoxCount = M;
  while (restBoxCount > 0) {
    answer++;
    for (let i=0; i<N; i++) {
      if (startIdxArr[i] < 0) continue;
      while (startIdxArr[i] > 0 && boxes[startIdxArr[i]] < 0) {
        startIdxArr[i]--;
      }
      if (boxes[startIdxArr[i]] > 0) {
        restBoxCount--;
        boxes[startIdxArr[i]] = -1;
        startIdxArr[i]--;
      }
    }
  }

  return answer;

  // upper-bound
  function BinarySearch(idx) {
    let [left, right] = [0, M - 1];
    let mid;
    while (left <= right) {
      mid = Math.floor((left + right) / 2);
      if (boxes[mid] <= cranes[idx]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return right;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
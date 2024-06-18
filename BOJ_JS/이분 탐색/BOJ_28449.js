/**
 * 제목 : 누가 이길까
 * 난이도 : 골드 5
 * 분류 : 이분 탐색(lowerBound, upperBound)
 */

const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [_, M] = convertToNumArr(input[0]);
  const codeA = convertToNumArr(input[1]);
  const codeB = convertToNumArr(input[2]);

  codeB.sort((a, b) => a - b);

  const getLowerBound = (a) => {
    let [left, right] = [0, M];
    let mid;
    while (left < right) {
      mid = Math.floor((left + right) / 2);
      if (codeB[mid] < a) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
  
  const getUpperBound = (a) => {
    let [left, right] = [0, M];
    let mid;
    while (left < right) {
      mid = Math.floor((left + right) / 2);
      if (codeB[mid] <= a) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }

  const answer = [0, 0, 0];

  for (const a of codeA) {
    const lower = getLowerBound(a);
    const upper = getUpperBound(a);
    answer[0] += lower;
    answer[1] += M - upper;
    answer[2] += upper - lower;
  }

  return answer.join(" ");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
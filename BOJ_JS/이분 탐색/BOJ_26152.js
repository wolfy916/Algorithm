/**
 * 제목 : 플래피 버드 스코어링
 * 난이도 : 실버 1
 * 분류 : 이분 탐색
 */

const convertToNumArr = (strArr) => strArr.split(" ").map((v) => +v);

const solution = (input) => {
  const [N, As, Bs, Q, Ws] = [
    +input[0],
    convertToNumArr(input[1]),
    convertToNumArr(input[2]),
    +input[3],
    convertToNumArr(input[4]),
  ];

  const passingSize = Array(N).fill(0).map((_, i) => As[i] - Bs[i]);
  for (let i = 0; i < N - 1; i++) {
    if (passingSize[i] < passingSize[i + 1]) {
      passingSize[i + 1] = passingSize[i];
    }
  }

  const answer = [];
  for (let i = 0; i < Q; i++) {
    let [left, right, value] = [0, N - 1, 0];
    let mid;
    while (left <= right) {
      mid = Math.floor((left + right) / 2);
      if (Ws[i] <= passingSize[mid]) {
        value = mid + 1;
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    answer.push(value);
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
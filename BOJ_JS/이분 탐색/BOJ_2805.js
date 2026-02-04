/**
 * 제목 : 나무 자르기
 * 난이도 : 실버 2
 * 분류 : 이진 탐색, 매개변수 탐색
 */

const solution = (input) => {
  const getNumberArray = (s) => s.split(" ").map(Number);

  let [n, m] = getNumberArray(input[0]);
  const trees = getNumberArray(input[1]);

  const isValid = (v) => {
    let sumV = 0;
    for (let i = 0; i < n; i++) {
      if (trees[i] > v) sumV += trees[i] - v;
    }
    return sumV >= m;
  };

  let answer = 0;
  let [left, right] = [0, 2_000_000_000];
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (isValid(mid)) {
      answer = Math.max(answer, mid);
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
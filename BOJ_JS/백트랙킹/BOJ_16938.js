/**
 * 제목 : 캠프 준비
 * 난이도 : 골드 5
 * 분류 : 백트랙킹
 */

const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [[N, L, R, X], A] = [
    convertToNumArr(input[0]),
    convertToNumArr(input[1]).sort((a, b) => a - b),
  ];

  const isSelected = Array.from({ length: N }, () => false);
  let answer = 0;

  const dfs = (minV, maxV, sumV, idx) => {
    if (sumV > R) return;
    if (L <= sumV && sumV <= R) {
      if (maxV !== sumV && maxV - minV >= X) {
        answer++;
      }
    }
    for (let i=idx; i<N; i++) {
      if (isSelected[i]) continue;
      isSelected[i] = true;
      dfs(Math.min(minV, A[i]), Math.max(maxV, A[i]), sumV + A[i], i + 1);
      isSelected[i] = false;
    }
  };

  dfs(1e9 + 1, 0, 0, 0);

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
/**
 * 제목 : 정수 삼각형
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const [n, triangle] = [+input[0], input.slice(1,).map(v => v.split(" ").map(v => +v))];
  const DP = Array.from({ length: n }, (_, i) => {
    return Array.from({ length: i + 1 }, () => 0);
  })
  DP[0][0] = triangle[0][0];
  for (let i=0; i<n-1; i++) {
    for (let j=0; j<i+1; j++) {
      DP[i + 1][j] = Math.max(DP[i + 1][j], DP[i][j] + triangle[i + 1][j]);
      DP[i + 1][j + 1] = Math.max(DP[i + 1][j + 1], DP[i][j] + triangle[i + 1][j + 1]);
    }
  }
  return Math.max(...DP[n-1]);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
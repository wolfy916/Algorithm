/**
 * 제목 : 카우버거 알바생
 * 난이도 : 골드 4
 * 분류 : 다이나믹 프로그래밍, 배낭 문제
 */

const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [[N, M, K], orders] = [
    convertToNumArr(input[0]),
    input.slice(1,).map(convertToNumArr),
  ];

  const dp = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: M + 1 }, () => {
      return Array.from({ length: K + 1 }, () => 0);
    });
  });

  for (let i=1; i<N + 1; i++) {
    const [a, b] = orders[i - 1];
    for (let m=1; m<M + 1; m++) {
      for (let k=1; k<K + 1; k++) {
        if (a > m || b > k) {
          dp[i][m][k] = dp[i - 1][m][k];
        } else {
          dp[i][m][k] = Math.max(dp[i - 1][m][k], 1 + dp[i - 1][m - a][k - b]);
        }
      }
    }
  }

  return dp[N][M][K];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
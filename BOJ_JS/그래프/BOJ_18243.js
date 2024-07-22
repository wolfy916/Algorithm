/**
 * 제목 : Small World Network
 * 난이도 : 실버 1
 * 분류 : 그래프, 플로이드-워셜
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, K] = convert(input[0]);
  const adjM = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: N + 1 }, () => Infinity);
  });

  for (let i = 1; i < K + 1; i++) {
    const [a, b] = convert(input[i]);
    adjM[a][b] = 1;
    adjM[b][a] = 1;
  }

  for (let i = 1; i < N + 1; i++) {
    adjM[i][i] = 0;
  }

  for (let k = 1; k < N + 1; k++) {
    for (let i = 1; i < N + 1; i++) {
      for (let j = 1; j < N + 1; j++) {
        adjM[i][j] = Math.min(adjM[i][j], adjM[i][k] + adjM[k][j]);
      }
    }
  }

  for (let i = 1; i < N + 1; i++) {
    for (let j = 1; j < N + 1; j++) {
      if (adjM[i][j] > 6) return "Big World!";
    }
  }

  return "Small World!";
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
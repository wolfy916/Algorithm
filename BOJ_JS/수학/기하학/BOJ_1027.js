/**
 * 제목 : 고층 건물
 * 난이도 : 골드 4
 * 분류 : 수학
 */

const solution = (input) => {
  const N = Number(input[0]);
  const heights = input[1].split(" ").map(Number);

  const countArr = Array.from({ length: N }, () => 0);
  for (let i=0; i<N-1; i++) {
    let maxV = -Infinity;
    for (let j=i + 1; j<N; j++) {
      const slope = getSlope(i, heights[i], j, heights[j]);
      if (maxV < slope) {
        maxV = slope;
        countArr[i]++;
        countArr[j]++;
      }
    }
  }

  return Math.max(...countArr);

  function getSlope(x1, y1, x2, y2) {
    if (y1 === y2) return 0;
    return (y1 - y2) / (x1 - x2);
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
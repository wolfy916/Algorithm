/**
 * 제목 : 좌표 압축
 * 난이도 : 실버 2
 * 분류 : 정렬, 좌표 압축
 */

const solution = (input) => {
  const coords = input[1].split(" ").map(Number);

  const sortedCoords = [...new Set(coords)].sort((a, b) => a - b)
  const countMap = new Map();
  
  sortedCoords.forEach((v, i) => countMap.set(v, i));

  return coords.map((v) => countMap.get(v)).join(" ");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
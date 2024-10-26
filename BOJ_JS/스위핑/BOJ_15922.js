/**
 * 제목 : 아우으 우아으이야!!
 * 난이도 : 골드 5
 * 분류 : 스위핑
 */

const solution = (input) => {
  const N = Number(input[0]);

  let [px, py] = input[1].split(" ").map(Number);
  let answer = py - px;
  let x, y;

  for (let i=2; i<N + 1; i++) {
    [x, y] = input[i].split(" ").map(Number);
    if (y <= py) continue;
    if (x < py) x = py;
    answer += y - x;
    px = x;
    py = y;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
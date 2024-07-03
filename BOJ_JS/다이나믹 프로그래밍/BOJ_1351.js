/**
 * 제목 : 무한 수열
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍, 해시를 사용한 집합과 맵
 */

const solution = (input) => {
  const [N, P, Q] = input[0].split(" ").map(Number);
  const memo = new Map();
  memo.set(0, 1);

  return getA(N);

  function getA(idx) {
    if (memo.get(idx)) return memo.get(idx);
    const value = getA(Math.floor(idx / P)) + getA(Math.floor(idx / Q));
    memo.set(idx, value);
    return value;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
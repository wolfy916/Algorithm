/**
 * 제목 : 사이클 게임
 * 난이도 : 골드 4
 * 분류 : 싸이클 검사, 유니온-파인드
 */

/**
 * 접근법
 * 1. 전형적인 union-find, 사이클 검사 문제
 * 2. 생각해보니 그래프를 구축할 필요가 없음
 */

const solution = (input) => {
  const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

  const [n, m] = convertToNumArr(input[0]);

  const par = Array.from({ length: n }, (_, i) => i);

  const find = (x) => {
    while (par[x] != x) x = par[par[x]];
    return x;
  }

  const union = (x, y) => par[Math.max(x, y)] = Math.min(x, y);

  for (let i=1; i<m + 1; i++) {
    const [x, y] = convertToNumArr(input[i]);
    const parX = find(x);
    const parY = find(y);
    if (parX != parY) union(parX, parY);
    else return i;
  }

  return 0;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
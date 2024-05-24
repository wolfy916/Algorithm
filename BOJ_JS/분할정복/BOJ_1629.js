/**
 * 제목 : 곱셈
 * 난이도 : 실버 1
 * 분류 : 분할 정복
 */

const solution = (input) => {
  let [A, B, C] = input[0].split(" ").map(v => +v);
  A = BigInt(A);
  C = BigInt(C);
  const pow = (exponent) => {
    if (exponent === 1) return A % C;
    const half = pow(Math.floor(exponent / 2));
    if (exponent % 2 === 0) return (half * half) % C;
    return (((half * half) % C) * (A % C)) % C;
  };
  return pow(B).toString();
}

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
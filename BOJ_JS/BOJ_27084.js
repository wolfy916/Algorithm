/**
 * 제목 : 카드 뽑기
 * 난이도 : 골드 5
 * 분류 : 수학(조합, 확률론)
 */

const solution = (input) => {
  const N = Number(input[0]);
  const cards = input[1].split(" ").map(Number);
  const counts = Array.from({ length: N + 1 }, () => 0n);
  
  for (const card of cards) counts[card]++;
  
  let answer = 1n;
  const mod = 1_000_000_007n;
  for (const count of counts) {
    answer *= count + 1n;
    answer %= mod;
  }

  return ((answer - 1n) % mod).toString();
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
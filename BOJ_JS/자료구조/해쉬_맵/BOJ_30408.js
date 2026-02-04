/**
 * 제목 : 춘배가 선물하는 특별한 하트
 * 난이도 : 골드 5
 * 분류 : 집합과 맵
 */

const solution = (input) => {
  let [n, m] = input[0].split(" ").map(v => BigInt(v));
  const set = new Set();
  set.add(n);

  while (n > 1n) {
    if (n % 2n === 1n) {
      n = (n - 1n) / 2n;
      set.add(n);
      set.add(n + 1n);

      n = n % 2n === 0n ? n + 1n : n;
    } else {
      n /= 2n;
      set.add(n);
    }
  }

  return set.has(m) ? "YES" : "NO";
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 레벨 햄버거
 * 난이도 : 골드 5
 * 분류 : 분할 정복
 */

const solution = (input) => {
  const [N, X] = input[0].split(" ").map(Number);
  const size = Array(N + 1);
  const patty = Array(N + 1);

  size[0] = 1n;
  patty[0] = 1n;

  for (let i = 1; i < N + 1; i++) {
    size[i] = size[i - 1] * 2n + 3n;
    patty[i] = patty[i - 1] * 2n + 1n;
  }

  return getPatty(N, BigInt(X)).toString();

  function getPatty(n, x) {
    if (x < 1n) return 0n;
    if (n === 0) return 1n;

    let count;
    if (x < size[n - 1] + 2n) {
      count = getPatty(n - 1, x - 1n);
    } else {
      count = patty[n - 1] + 1n;
      count += getPatty(n - 1, x - size[n - 1] - 2n);
    }

    return count;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 선물할인
 * 난이도 : 실버 1
 * 분류 : 그리디
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  let [n, b, a] = convert(input[0]);
  const arr = convert(input[1]);

  arr.sort((a, b) => a - b);

  let left = 0;
  let right = 0;
  for (let i = 0; i < a; i++) {
    b -= arr[i] / 2;
    right = i + 1;
    if (b < 0) return i;
  }

  while (right < n) {
    if (right - left < a) {
      b -= arr[right] / 2;
      if (b < 0) break;
      right++;
    } else {
      if (a > 0) {
        b -= arr[left] / 2;
        left++;
      } else {
        b -= arr[right];
        if (b < 0) break;
        right++;
      }
    }
  }

  return right;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
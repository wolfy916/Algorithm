/**
 * 제목 : 약수의 합
 * 난이도 : 골드 4
 * 분류 : 누적합, 수학(소수 판정)
 */

const solution = (input) => {
  const f = Array.from({ length: 1e6 + 1 }, (_, i) => i + 1);
  f[1] = 1;

  for (let i = 2; i < 1e6 + 1; i++) {
    let j = 1;
    while (i * ++j < 1e6 + 1) {
      f[i * j] += i;
    }
  }

  for (let i = 2; i < 1e6 + 1; i++) {
    f[i] += f[i - 1];
  }

  let idx = 1;
  let T = Number(input[0]);
  const answer = [];
  while (T--) {
    const N = Number(input[idx++]);
    answer.push(f[N]);
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
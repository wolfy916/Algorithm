/**
 * 제목 : 즐거운 회의
 * 난이도 : 골드 5
 * 분류 : 누적합
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const [N, M, T] = convert(input[0]);
  const info = input.slice(1, N + 1).map(convert);
  const table = Array.from(Array(T + 1), () => 0);

  for (let i = N + 1; i < N + M + 1; i++) {
    const [c, d] = convert(input[i]);
    if (info[c - 1][1] <= info[d - 1][0] || info[d - 1][1] <= info[c - 1][0]) continue;
    table[Math.max(info[c - 1][0], info[d - 1][0])] += 1;
    table[Math.min(info[c - 1][1], info[d - 1][1])] -= 1;
  }

  for (let i = 1; i < T + 1; i++) {
    table[i] += table[i - 1];
  }

  table.pop();

  return table.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
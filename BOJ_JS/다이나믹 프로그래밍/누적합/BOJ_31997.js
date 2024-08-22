/**
 * 제목 : 즐거운 회의
 * 난이도 : 골드 5
 * 분류 : 누적합
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const [N, M, T] = convert(input[0]);
  const info = input.slice(1, N + 1).map(convert);
  const adjL = Array.from(Array(N + 1), () => []);
  const used = Array.from(Array(N + 1), () => false);
  const table = Array.from(Array(T + 1), () => 0);

  for (let i = N + 1; i < N + M + 1; i++) {
    const [c, d] = convert(input[i]);
    adjL[c].push(d);
    adjL[d].push(c);
  }

  for (let i = 1; i < N + 1; i++) {
    used[i] = true;
    for (const j of adjL[i]) {
      if (used[j]) continue;
      if (info[i - 1][1] <= info[j - 1][0] || info[j - 1][1] <= info[i - 1][0])
        continue;
      table[Math.max(info[i - 1][0], info[j - 1][0])] += 1;
      table[Math.min(info[i - 1][1], info[j - 1][1])] -= 1;
    }
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
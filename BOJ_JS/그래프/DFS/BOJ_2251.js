/**
 * 제목 : 물통
 * 난이도 : 골드 5
 * 분류 : DFS
 */

const solution = (input) => {
  const max = input[0].split(" ").map(Number);
  const visited = Array.from(Array(max[0] + 1), () => {
    return Array.from(Array(max[1] + 1), () => Array(max[2] + 1).fill(false));
  });
  const answerSet = new Set();

  dfs([0, 0, max[2]]);

  const answer = Array.from(answerSet);

  answer.sort((a, b) => a - b);

  return answer.join(" ");

  function dfs(v) {
    if (visited[v[0]][v[1]][v[2]]) return;
    visited[v[0]][v[1]][v[2]] = true;

    if (v[0] === 0) answerSet.add(v[2]);

    let d;
    for (let i = 0; i < 3; i++) {
      if (v[i] === 0) continue;
      for (let j = 0; j < 3; j++) {
        if (i === j || v[j] === max[j]) continue;
        d = Math.min(v[i], max[j] - v[j]);
        v[i] -= d;
        v[j] += d;
        dfs(v);
        v[i] += d;
        v[j] -= d;
      }
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
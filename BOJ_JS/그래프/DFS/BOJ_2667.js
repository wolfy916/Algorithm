/**
 * 제목 : 단지번호붙이기
 * 난이도 : 실버 1
 * 분류 : DFS
 */

const solution = (input) => {
  const N = Number(input[0]);
  const board = input.slice(1,).map((v) => v.split("").map(Number));
  const visited = Array.from(Array(N), () => Array(N).fill(false));
  const delta = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  const nums = [];


  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (board[i][j] === 0 || visited[i][j]) continue;
      visited[i][j] = true;
      nums.push(dfs(i, j));
    }
  }

  nums.sort((a, b) => a - b);

  return `${nums.length}\n${nums.join("\n")}`;

  function dfs(vi, vj) {
    let count = 1;
    for (const [di, dj] of delta) {
      const ni = vi + di;
      const nj = vj + dj;
      if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
      if (board[ni][nj] === 0 || visited[ni][nj]) continue;
      visited[ni][nj] = true;
      count += dfs(ni, nj);
    }
    return count;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
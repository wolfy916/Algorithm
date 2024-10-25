/**
 * 제목 : 유기농 배추
 * 난이도 : 실버 2
 * 분류 : DFS
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const answer = [];
  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];

  let M, N, K, area, 
    idx = 0,
    T = Number(input[idx++]);
  while (T--) {
    [M, N, K] = convert(input[idx++]);
    area = Array.from(Array(N), () => Array(M).fill(0));

    while (K--) {
      const [j, i] = convert(input[idx++]);
      area[i][j] = 1;
    }

    let count = 0;
    for (let i=0; i<N; i++) {
      for (let j=0; j<M; j++) {
        if (area[i][j] === 1) {
          dfs(i, j);
          count += 1;
        }
      }
    }
    answer.push(count);
  }

  return answer.join("\n");

  function dfs(vi, vj) {
    area[vi][vj] = 2;

    for (let k=0; k<4; k++) {
      const ni = vi + di[k];
      const nj = vj + dj[k];
      if (ni < 0 || nj < 0 || ni >= N || nj >= M) continue;
      if (area[ni][nj] !== 1) continue;
      dfs(ni, nj);
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
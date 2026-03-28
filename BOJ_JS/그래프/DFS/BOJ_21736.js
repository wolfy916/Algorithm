/**
 * 제목 : 헌내기는 친구가 필요해
 * 난이도 : 실버 2
 * 분류 : DFS
 */

const solution = (input) => {
  const [n, m] = input[0].split(" ").map(Number);
  const campus = Array.from({ length: n }, (_, i) => {
    return input[i + 1];
  });

  
  let si, sj;
  outer: for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (campus[i][j] === "I") {
        si = i;
        sj = j;
        break outer;
      }
    }
  }

  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];
  const isInvalid = (i, j) => i < 0 || i >= n || j < 0 || j >= m;

  let answer = 0;
  const visited = Array.from({ length: n }, () => {
    return Array.from({ length: m }, () => false);
  });

  const dfs = (vi, vj) => {
    if (isInvalid(vi, vj) || visited[vi][vj] || campus[vi][vj] === "X") return;
    if (campus[vi][vj] === "P") answer++;

    visited[vi][vj] = true;

    for (let k = 0; k < 4; k++) {
      const ni = vi + di[k];
      const nj = vj + dj[k];

      dfs(ni, nj);
    }
  };

  dfs(si, sj);

  return answer === 0 ? "TT" : answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

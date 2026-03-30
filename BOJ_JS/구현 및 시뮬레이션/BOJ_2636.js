/**
 * 제목 : 치즈
 * 난이도 : 골드 4
 * 분류 : 구현, 시뮬레이션
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);

  const [n, m] = convert(input[0]);
  const board = Array.from({ length: n }, (_, i) => convert(input[i + 1]));

  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];
  const isInvalid = (i, j) => i < 0 || j < 0 || i >= n || j >= m;

  const visited = Array.from({ length: n }, () => Array(m));
  const checkMeltingCheeze = (vi = 0, vj = 0) => {
    visited[vi][vj] = true;

    if (board[vi][vj] === 1) {
      board[vi][vj] = 2;
      return;
    }

    for (let k = 0; k < 4; k++) {
      const ni = vi + di[k];
      const nj = vj + dj[k];

      if (isInvalid(ni, nj) || visited[ni][nj]) continue;

      checkMeltingCheeze(ni, nj);
    }
  };

  let time = 0;
  let remainingCheeze = board.reduce(
    (a, c) => a + c.filter((v) => v > 0).length,
    0,
  );
  let lastMeltingCheeze = 0;

  while (remainingCheeze > 0) {
    visited.forEach((v) => v.fill(false));
    time++;
    lastMeltingCheeze = 0;

    checkMeltingCheeze();

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) {
        if (board[i][j] === 2) {
          board[i][j] = 0;
          lastMeltingCheeze++;
        }
      }
    }

    remainingCheeze -= lastMeltingCheeze;
  }

  const answer = `${time}\n${lastMeltingCheeze}`

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
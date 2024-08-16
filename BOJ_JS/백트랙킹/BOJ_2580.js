/**
 * 제목 : 스도쿠
 * 난이도 : 골드 4
 * 분류 : 백트랙킹
 */

const solution = (input) => {
  const sudoku = input.map((v) => v.split(" ").map(Number));

  const blanks = [];
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (sudoku[i][j] === 0) {
        blanks.push([i, j]);
      }
    }
  }

  dfs(0);

  return sudoku.map((v) => v.join(" ")).join("\n");

  function checkRow(r, n) {
    for (let j = 0; j < 9; j++) {
      if (sudoku[r][j] === n) return false;
    }
    return true;
  }

  function checkCol(c, n) {
    for (let i = 0; i < 9; i++) {
      if (sudoku[i][c] === n) return false;
    }
    return true;
  }

  function checkSquare(r, c, n) {
    const si = r - (r % 3);
    const sj = c - (c % 3);
    for (let i = si; i < si + 3; i++) {
      for (let j = sj; j < sj + 3; j++) {
        if (sudoku[i][j] === n) return false;
      }
    }
    return true;
  }

  function dfs(idx) {
    if (idx === blanks.length) return true;

    const r = blanks[idx][0];
    const c = blanks[idx][1];
    for (let num = 1; num < 10; num++) {
      if (checkRow(r, num) && checkCol(c, num) && checkSquare(r, c, num)) {
        sudoku[r][c] = num;
        if (dfs(idx + 1)) return true;
        sudoku[r][c] = 0;
      }
    }

    return false;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
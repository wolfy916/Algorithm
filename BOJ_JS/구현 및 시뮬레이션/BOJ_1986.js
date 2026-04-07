/**
 * 제목 : 체스
 * 난이도 : 실버 1
 * 분류 : 구현
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M] = convert(input[0]);

  const isInvalid = (i, j) => i < 0 || j < 0 || i >= N || j >= M;
  const board = Array.from({ length: N }, () => {
    return Array.from({ length: M }, () => 0);
  });

  const queens = convert(input[1]);
  const knights = convert(input[2]);
  const pawns = convert(input[3]);

  const place = (pieces, number) => {
    for (let i = 1; i < pieces.length; i += 2) {
      const vi = pieces[i] - 1;
      const vj = pieces[i + 1] - 1;

      board[vi][vj] = number;
    }
  };

  const generateQueenArea = (i, j) => {
    const di = [-1, -1, 1, 1, -1, 1, 0, 0];
    const dj = [-1, 1, -1, 1, 0, 0, -1, 1];

    for (let k = 0; k < 8; k++) {
      let ni = i + di[k];
      let nj = j + dj[k];

      while (true) {
        if (isInvalid(ni, nj) || board[ni][nj] > 0) break;

        board[ni][nj] = -1;

        ni += di[k];
        nj += dj[k];
      }
    }
  };

  const generateKnightArea = (i, j) => {
    const di = [-1, -2, -2, -1, 1, 2, 2, 1];
    const dj = [-2, -1, 1, 2, 2, 1, -1, -2];

    for (let k = 0; k < 8; k++) {
      const ni = i + di[k];
      const nj = j + dj[k];

      if (isInvalid(ni, nj) || board[ni][nj] > 0) continue;

      board[ni][nj] = -1;
    }
  };

  const generate = [null, generateQueenArea, generateKnightArea];

  place(queens, 1);
  place(knights, 2);
  place(pawns, 3);

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (board[i][j] < 1 || board[i][j] === 3) continue;
      generate[board[i][j]](i, j);
    }
  }

  const answer = board.reduce((a, c) => a + c.filter(v => v === 0).length, 0);

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
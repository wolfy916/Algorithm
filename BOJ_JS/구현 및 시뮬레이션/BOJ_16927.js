/**
 * 제목 : 배열 돌리기 2
 * 난이도 : 골드 5
 * 분류 : 구현
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M, R] = convert(input.shift());

  for (let i = 0; i < N; i++) input[i] = convert(input[i]);

  const numOfSquare = Math.floor(Math.min(N, M) / 2);
  const squares = Array.from(Array(numOfSquare), () => []);
  const di = [1, 0, -1, 0];
  const dj = [0, 1, 0, -1];
  let s = 0;
  let i, j, k, squareSize;

  while (s < numOfSquare) {
    i = s;
    j = s;
    k = 0;
    squareSize = (N - s * 2) * 2 + (M - s * 2) * 2 - 4;
    while (squares[s].length < squareSize) {
      squares[s].push([i, j]);
      if (!isValid(i + di[k], j + dj[k], s)) k = (k + 1) % 4;
      i += di[k];
      j += dj[k];
    }
    s++;
  }

  const answer = Array.from(Array(N), () => Array(M));
  let ni, nj;
  for (let s = 0; s < numOfSquare; s++) {
    for (let k = 0; k < squares[s].length; k++) {
      [i, j] = squares[s][k];
      [ni, nj] = squares[s][(k + R) % squares[s].length];
      answer[ni][nj] = input[i][j];
    }
  }

  return answer.map((v) => v.join(" ")).join("\n");

  function isValid(i, j, s) {
    return i < s || j < s || i >= N - s || j >= M - s ? false : true;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
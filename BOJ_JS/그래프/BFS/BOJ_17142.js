/**
 * 제목 : 연구소 3
 * 난이도 : 골드 3
 * 분류 : bfs
 */

const convertToNumArr = (str) => str.split(" ").map((v) => +v);

const solution = (input) => {
  const [[N, M], ...lab] = [
    [...convertToNumArr(input[0])],
    ...input.slice(1).map((v) => convertToNumArr(v)),
  ];
  const INF = 2501;
  const K = lab.reduce((acc, cur) => acc + cur.filter((v) => v > 1).length, 0);
  const board = Array.from({ length: N }, () => {
    return Array.from({ length: N }, () => Array(K).fill(INF));
  });
  const delta = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  const bfs = (vIdx, si, sj) => {
    const queue = [[si, sj]];
    board[si][sj][vIdx] = 0;
    while (queue.length > 0) {
      const [vi, vj] = queue.shift();
      for (const [di, dj] of delta) {
        const [ni, nj] = [vi + di, vj + dj];
        if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
        if (lab[ni][nj] === 1) continue;
        if (board[ni][nj][vIdx] < INF) continue;
        board[ni][nj][vIdx] = board[vi][vj][vIdx] + 1;
        queue.push([ni, nj]);
      }
    }
  };

  let virusIdx = -1;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (lab[i][j] === 2) {
        bfs(++virusIdx, i, j);
      }
    }
  }

  // console.log(board);

  let answer = INF;
  let combArr = [];

  const compare = () => {
    let value = 0;
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (lab[i][j] === 0) {
          let minV = combArr.reduce(
            (acc, cur) => Math.min(acc, board[i][j][cur]),
            INF
          );
          if (minV === INF) return INF;
          value = Math.max(value, minV);
        }
      }
    }
    return value;
  };

  const comb = (s, cnt) => {
    if (cnt >= M) {
      answer = Math.min(answer, compare());
      return;
    }
    for (let i = s; i < K - M + 1 + cnt; i++) {
      if (cnt < M) {
        combArr.push(i);
        comb(i + 1, cnt + 1);
        combArr.pop();
      }
    }
  };

  comb(0, 0);

  return answer < INF ? answer : -1;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));

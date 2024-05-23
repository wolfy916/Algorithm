/**
 * 제목 : 토마토
 * 난이도 : 골드 5
 * 분류 : bfs
 */

/**
 * 접근 방법
 * 1. 3차원 배열을 2차원 배열로 표현(상하좌우 이동으로 경계를 넘으면 층이동으로 인식될 수 있음을 주의)
 * 2. queue.shift()를 인덱싱으로 고치니 통과..
 */

const solution = (input) => {
  const convertToNumArr = (strArr) => strArr.split(" ").map((v) => +v);

  const [[M, N, H], tomatos] = [
    convertToNumArr(input[0]),
    input.slice(1).map((v) => convertToNumArr(v)),
  ];

  let target = 0;
  const queue = [];
  for (let i = 0; i < N * H; i++) {
    for (let j = 0; j < M; j++) {
      if (tomatos[i][j] === 1) {
        queue.push([i, j]);
      } else if (tomatos[i][j] === 0) {
        target++;
      }
    }
  }

  const delta = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [N, 0],
    [-N, 0],
  ];

  let idx = 0;
  while (queue.length > idx && target > 0) {
    const [vi, vj] = queue[idx++];
    for (const [di, dj] of delta) {
      const [ni, nj] = [vi + di, vj + dj];
      const h = Math.floor(vi / N);
      if (Math.abs(di) === N) {
        if (ni < 0 || nj < 0 || ni >= H * N || nj >= M) continue;
      } else {
        if (ni < h * N || nj < 0 || ni >= (h + 1) * N || nj >= M) continue;
      }
      if (tomatos[ni][nj] === 0) {
        tomatos[ni][nj] = tomatos[vi][vj] + 1;
        queue.push([ni, nj]);
        target--;
      }
    }
  }

  return target > 0 ? -1 : Math.max(...tomatos.map((v) => Math.max(...v))) - 1;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));

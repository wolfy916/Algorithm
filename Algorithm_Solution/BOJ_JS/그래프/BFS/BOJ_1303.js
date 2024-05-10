/**
 * 제목 : 전쟁 - 전투 - 백준 실버 1
 * 분류 : 완전 탐색, BFS
 */

/**
 * 접근 방식
 * 1. 2차원 배열에서 BFS 카운팅
 */

const solution = (input) => {
  // 데이터 초기화
  let line = 0;
  const [M, N] = input[line++].split(" ").map((v) => Number(v));
  const ground = Array(N);
  for (let i = 0; i < N; i++) {
    ground[i] = input[line++].trim();
  }
  const delta = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  const visited = Array.from({ length: N }, () => {
    return Array.from({ length: M }, () => false);
  });
  let answer = { W: 0, B: 0 };

  // 로직 수행
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (visited[i][j]) continue;
      bfs(i, j, ground[i][j]);
    }
  }
  return `${answer.W} ${answer.B}`;

  // [1] BFS 함수
  function bfs(i, j, color) {
    let count = 1;
    let queue = [[i, j]];
    visited[i][j] = true;
    while (queue.length > 0) {
      let [vi, vj] = queue.shift();
      for (let [di, dj] of delta) {
        let [ni, nj] = [vi + di, vj + dj];
        if (ni < 0 || nj < 0 || ni >= N || nj >= M) continue;
        if (visited[ni][nj]) continue;
        if (ground[ni][nj] != color) continue;
        visited[ni][nj] = true;
        count++;
        queue.push([ni, nj]);
      }
    }
    answer[color] += count ** 2;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
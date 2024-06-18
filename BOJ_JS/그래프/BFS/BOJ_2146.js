/**
 * 제목 : 다리 만들기
 * 난이도 : 골드 3
 * 분류 : bfs
 */

const solution = (input) => {
  const N = Number(input[0]);
  const area = input.slice(1).map((v) => v.split(" ").map(Number));

  const delta = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const visited = Array.from({ length: N }, () => {
    return Array.from({ length: N }, () => false);
  });
  const islands = [[]];

  const grouping = (vi, vj, g) => {
    if (visited[vi][vj]) return;

    visited[vi][vj] = true;
    area[vi][vj] = g;
    islands[g].push([vi, vj]);

    for (const [di, dj] of delta) {
      const [ni, nj] = [vi + di, vj + dj];
      if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
      if (area[ni][nj] < 1) continue;
      grouping(ni, nj, g);
    }
  };

  let answer = Number.MAX_SAFE_INTEGER;
  let group = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (area[i][j] < 1) continue;
      if (visited[i][j]) continue;
      islands.push([]);
      grouping(i, j, ++group);
    }
  }

  const bfs = (g) => {
    const len = islands[g].length;
    let nextG = 0;
    for (let i = 0; i < len; i++) {
      const [vi, vj] = islands[g].shift();
      for (const [di, dj] of delta) {
        const [ni, nj] = [vi + di, vj + dj];
        if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
        if (area[ni][nj] > 0 && area[ni][nj] !== g)
          nextG = Math.max(nextG, area[ni][nj]);
        if (area[ni][nj] < 1) {
          area[ni][nj] = g;
          islands[g].push([ni, nj]);
        }
      }
    }

    return nextG;
  };

  let depth = 1;
  while (true) {
    let flag = false;
    for (let i = 1; i < islands.length; i++) {
      const g = bfs(i);
      if (g > 0) {
        flag = true;
        answer = Math.min(answer, i < g ? depth * 2 - 2 : depth * 2 - 1);
      }
    }
    if (flag) break;
    depth++;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
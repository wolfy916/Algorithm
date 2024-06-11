/**
 * 제목 : 나의 인생에는 수학과 함께
 * 난이도 : 골드 5
 * 분류 : dfs, 백트랙킹, 브루트포스
 */

const solution = (input) => {
  const [N, board] = [
    Number(input[0]),
    input.slice(1,).map(v => v.trim().split(" ")),
  ];

  const ref = {
    "+": (a, b) => a + b,
    "-": (a, b) => a - b,
    "*": (a, b) => a * b,
  };
  const delta = [[1, 0], [0, 1]];
  const visited = Array.from({ length: N }, () => {
    return Array.from({ length: N }, () => false);
  });
  const answer = [-Infinity, Infinity];

  const dfs = (value, vi, vj, mathSign, isNumber) => {
    if (vi === N - 1 && vj === N - 1) {
      answer[0] = Math.max(answer[0], value);
      answer[1] = Math.min(answer[1], value);
      return;
    }

    for (const [di, dj] of delta) {
      const [ni, nj] = [vi + di, vj + dj];
      if (ni >= N || nj >= N) continue;
      if (visited[ni][nj]) continue;
      visited[ni][nj] = true;
      dfs(
        isNumber ? value : ref[mathSign](value, Number(board[ni][nj])),
        ni,
        nj,
        isNumber ? board[ni][nj] : mathSign,
        !isNumber
      );
      visited[ni][nj] = false;
    }
  };

  dfs(Number(board[0][0]), 0, 0, '+', true);

  return answer.join(" ");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
/**
 * 제목 : 이동하기
 * 난이도 : 실버 2
 * 분류 : 누적합
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const [N, M] = convert(input[0]);
  const maze = input.slice(1).map(convert);
  
    for (let i = 1; i < N; i++) {
      maze[i][0] += maze[i - 1][0];
    }

  for (let j = 1; j < M; j++) {
    maze[0][j] += maze[0][j - 1];
  }

  for (let i = 1; i < N; i++) {
    for (let j = 1; j < M; j++) {
      maze[i][j] += Math.max(maze[i - 1][j - 1], maze[i - 1][j], maze[i][j - 1]);
    }
  }

  return maze[N - 1][M - 1];
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 체스판 다시 칠하기 2
 * 난이도 : 골드5
 * 분류 : 누적합
 */

const solution = (input) => {
  let line = 0;
  const [N, M, K] = input[line++].split(" ").map((v) => +v);
  const board = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: M + 1 }, () => 0);
  });

  let [b, w] = [1, 0];
  for (let i = 1; i < N + 1; i++) {
    const target = input[line++].trim();
    for (let j = 1; j < M + 1; j++) {
      if (
        (j % 2 === b && target[j - 1] === "B") ||
        (j % 2 === w && target[j - 1] === "W")
      ) {
        board[i][j] += board[i][j - 1] + board[i - 1][j] - board[i - 1][j - 1];
      } else {
        board[i][j] +=
          board[i][j - 1] + board[i - 1][j] - board[i - 1][j - 1] + 1;
      }
    }
    [b, w] = [w, b];
  }

  let answer = 10e9;
  let cnt;
  for (let i=K; i<N+1; i++) {
    for (let j=K; j<M+1; j++) {
      cnt = Math.abs(board[i][j] - board[i-K][j] - board[i][j-K] + board[i-K][j-K]);
      answer = Math.min(cnt, Math.pow(K, 2) - cnt, answer);
    }
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
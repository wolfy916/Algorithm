/**
 * 제목 : 오목
 * 난이도 : 골드 5
 * 분류 : 브루트포스
 */

const solution = (input) => {
  const board = Array.from({ length: 19 }, (_, i) => {
    return input[i].split(" ").map(Number);
  });

  const dp = Array.from({ length: 19 }, () => {
    return Array.from({ length: 19 }, () => {
      return [1, 1, 1, 1];
    });
  });

  for (let i = 18; i >= 1; i--) {
    for (let j = 0; j < 19; j++) {
      if (board[i][j] === 0) continue;
      if (board[i][j] !== board[i - 1][j]) continue;
      dp[i - 1][j][0] += dp[i][j][0];
    }
  }

  for (let i = 0; i < 19; i++) {
    for (let j = 18; j >= 1; j--) {
      if (board[i][j] === 0) continue;
      if (board[i][j] !== board[i][j - 1]) continue;
      dp[i][j - 1][1] += dp[i][j][1];
    }
  }

  for (let i = 18; i >= 1; i--) {
    for (let j = 18; j >= 1; j--) {
      if (board[i][j] === 0) continue;
      if (board[i][j] !== board[i - 1][j - 1]) continue;
      dp[i - 1][j - 1][2] += dp[i][j][2];
    }
  }

  for (let i = 0; i < 18; i++) {
    for (let j = 18; j >= 1; j--) {
      if (board[i][j] === 0) continue;
      if (board[i][j] !== board[i + 1][j - 1]) continue;
      dp[i + 1][j - 1][3] += dp[i][j][3];
    }
  }

  for (let i = 0; i < 19; i++) {
    for (let j = 0; j < 19; j++) {
      if (board[i][j] === 0) continue;
      if (
        (dp[i][j][0] === 5 && 
          (i === 0 || board[i][j] !== board[i - 1][j])) ||
        (dp[i][j][1] === 5 && 
          (j === 0 || board[i][j] !== board[i][j - 1])) ||
        (dp[i][j][2] === 5 &&
          (i === 0 || j === 0 || board[i][j] !== board[i - 1][j - 1])) ||
        (dp[i][j][3] === 5 &&
          (i === 18 || j === 0 || board[i][j] !== board[i + 1][j - 1]))
      )
        return `${board[i][j]}\n${i + 1} ${j + 1}`;
    }
  }

  return "0";
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
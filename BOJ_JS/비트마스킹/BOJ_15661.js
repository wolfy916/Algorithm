/**
 * 제목 : 링크와 스타트
 * 난이도 : 골드 5
 * 분류 : 비트마스킹
 */

/**
 * 접근 방식
 * 1. N = 4라면, 4개의 비트로 2 ** N개의 조합을 표현 가능
 * 2. 표현한 팀 조합의 능력치값을 1차원 배열(=score)로 표현
 */

const solution = (input) => {
  const N = +input[0];
  const board = input.slice(1).map((v) => v.split(" ").map(Number));
  const score = Array.from({ length: 2 ** N }, () => 0);

  const dfs = (teamBit, index = 0, count = 0) => {
    if (count === N) return;

    for (let i = index; i < N; i++) {
      const nextTeamBit = teamBit | (1 << i);
      score[nextTeamBit] = score[teamBit];
      for (let j = 0; j < N; j++) {
        if (teamBit & (1 << j)) {
          score[nextTeamBit] += board[i][j] + board[j][i];
        }
      }

      dfs(nextTeamBit, i + 1, count + 1);
    }
  };

  dfs(0);

  let answer = Number.MAX_SAFE_INTEGER;
  const MAX = score.length - 1;
  for (let i = 1; i < score.length / 2 + 1; i++) {
    const diff = Math.abs(score[i] - score[MAX - i]);
    answer = Math.min(answer, diff);
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));

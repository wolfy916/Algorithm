/**
 * 제목 : 스타트와 링크
 * 난이도 : 실버 1
 * 분류 : 백트랙킹, 브루트포스
 */

const solution = (input) => {
  const N = Number(input[0]);
  const table = input.slice(1).map((v) => v.split(" ").map(Number));

  let tmp;
  for (let i = 0; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {
      tmp = table[i][j];
      table[i][j] += table[j][i];
      table[j][i] += tmp;
    }
  }

  let answer = Infinity;
  const isStartTeam = Array(N).fill(false);
  getStartTeam(0, 0);

  return answer;

  function calculateScore() {
    let result = 0;
    for (let i = 0; i < N - 1; i++) {
      for (let j = i + 1; j < N; j++) {
        if (isStartTeam[i] !== isStartTeam[j]) continue;
        if (isStartTeam[i]) result += table[i][j];
        else result -= table[i][j];
      }
    }
    return Math.abs(result);
  }

  function getStartTeam(n, count) {
    if (count === N / 2) {
      answer = Math.min(answer, calculateScore());
      return;
    }

    if (n >= N) return;

    // 팀원 합류
    isStartTeam[n] = true;
    getStartTeam(n + 1, count + 1);
    isStartTeam[n] = false;

    // 다음 팀원으로 패스
    getStartTeam(n + 1, count);
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
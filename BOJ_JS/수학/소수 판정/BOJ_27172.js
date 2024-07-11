/**
 * 제목 : 수 나누기 게임
 * 난이도 : 골드 5
 * 분류 : 수학(소수 판정, 에라토스테네스의 체)
 */

const solution = (input) => {
  const N = Number(input[0]);
  const players = input[1].split(" ").map(Number);

  const playerCard = Array.from({ length: 1e6 + 1 }, () => -1);
  for (let i = 0; i < N; i++) {
    const x = players[i];
    playerCard[x] = i;
  }

  const scores = Array(N).fill(0);
  for (let i = 0; i < playerCard.length; i++) {
    const playerIdx = playerCard[i];
    if (playerIdx === -1) continue;
    for (let j = i * 2; j < playerCard.length; j += i) {
      const otherPlayerIdx = playerCard[j];
      if (otherPlayerIdx === -1) continue;
      scores[playerIdx]++;
      scores[otherPlayerIdx]--;
    }
  }

  return scores.join(" ");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
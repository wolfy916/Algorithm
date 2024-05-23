/**
 * 제목 : 경로 찾기
 * 난이도 : 실버 1
 * 분류 : 플로이드 워셜
 */

const solution = (input) => {
  const [N, G] = [
    +input[0],
    input.slice(1).map((v) => v.split(" ").map((v) => +v)),
  ];

  for (let r = 0; r < N; r++) {
    for (let a = 0; a < N; a++) {
      for (let b = 0; b < N; b++) {
        if (G[a][r] > 0 && G[r][b] > 0) G[a][b] = 1;
      }
    }
  }

  const answer = G.map((v) => v.join(" ")).join("\n");

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
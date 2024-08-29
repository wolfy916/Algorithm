/**
 * 제목 : LCA
 * 난이도 : 골드 3
 * 분류 : 트리, 최소 공통 조상(LCA)
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const N = Number(input[0]);
  const adjL = Array.from(Array(N + 1), () => []);

  let a, b;
  for (let i = 1; i < N; i++) {
    [a, b] = convert(input[i]);
    adjL[a].push(b);
    adjL[b].push(a);
  }

  const level = Array(N + 1).fill(0);
  const par = Array(N + 1).fill(0);
  par[1] = 1;
  setLevelAndPar(1, 1);

  const answer = [];
  const M = Number(input[N]);
  for (let i = N + 1; i < N + M + 1; i++) {
    [a, b] = convert(input[i]);

    while (level[a] > level[b]) {
      a = par[a];
    }
    while (level[a] < level[b]) {
      b = par[b];
    }

    while (a !== b) {
      a = par[a];
      b = par[b];
    }

    answer.push(a);
  }

  return answer.join("\n");

  function setLevelAndPar(v, l) {
    level[v] = l;
    for (const w of adjL[v]) {
      if (level[w]) continue;
      par[w] = v;
      setLevelAndPar(w, l + 1);
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
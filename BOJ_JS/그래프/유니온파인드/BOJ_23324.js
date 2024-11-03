/**
 * 제목 : 어려운 모든 정점 쌍 최단 거리
 * 난이도 : 골드 4
 * 분류 : 유니온 파인드
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M, K] = convert(input[0]);
  const par = Array.from(Array(N + 1), (_, i) => i);

  let x, y, parX, parY;
  for (let i = 1; i < M + 1; i++) {
    if (i === K) continue;
    [x, y] = convert(input[i]);
    parX = findParent(x);
    parY = findParent(y);
    if (parX !== parY) union(parX, parY);
  }

  let count = 0;
  const parV = par[1];
  for (let i = 1; i < N + 1; i++) {
    if (parV === findParent(i)) count++;
  }

  return count * (N - count);

  function findParent(x) {
    while (x !== par[x]) {
      x = par[par[x]];
    }
    return x;
  }

  function union(x, y) {
    if (x <= y) par[y] = x;
    else par[x] = y;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
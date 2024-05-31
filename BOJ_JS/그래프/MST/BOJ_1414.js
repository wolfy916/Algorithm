/**
 * 제목 : 불우이웃돕기
 * 난이도 : 골드3
 * 분류 : MST(prim)
 */

const solution = (input) => {
  const N = +input[0];
  const adjM = Array.from({ length: N }, () => {
    return Array.from({ length: N }, () => 0);
  });

  let total = 0;
  for (let i=0; i<N; i++) {
    for (let j=0; j<N; j++) {
      if (input[i + 1][j] === "0") continue;
      let weight = input[i + 1][j].charCodeAt();
      weight -= weight <= 90 ? 38 : 96;
      total += weight;
      if (adjM[i][j] < 1 || adjM[i][j] > weight) {
        adjM[i][j] = weight;
        adjM[j][i] = weight;
      }
    }
  }

  const prim = (r, V) => {
    const visited = Array(V).fill(false);
    visited[r] = true;
    let sumV = 0;
    for (let _ = 0; _ < V - 1; _++) {
      let nxt = 0;
      let minV = 150;
      for (let i = 0; i < V; i++) {
        if (visited[i]) {
          for (let j = 0; j < V; j++) {
            if (adjM[i][j] > 0 && !visited[j] && minV > adjM[i][j]) {
              nxt = j;
              minV = adjM[i][j];
            }
          }
        }
      }
      sumV += minV;
      visited[nxt] = true;
    }
    return visited.includes(false) ? -1 : total - sumV;
  };

  return prim(0, N);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
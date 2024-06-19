/**
 * 제목 : 그래프 탐색
 * 난이도 : 골드 5
 * 분류 : bfs
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [n, m] = convert(input[0]);
  const edges = input.slice(1, m + 1).map(convert);
  const q = convert(input[m + 1]);
  const plans = input.slice(m + 2, m + q + 2).map(convert);

  const adjM = Array.from({ length: n + 1 }, () => {
    return Array.from({ length: n + 1 }, () => 0);
  });

  for (const [a, b] of edges) {
    adjM[a][b] = 1;
    adjM[b][a] = 1;
  }

  const bfs = () => {
    const dis = Array.from({ length: n + 1 }, () => -1);
    dis[1] = 0;
    const queue = [1];
    while (queue.length > 0) {
      const v = queue.shift();
      for (let w = 1; w < n + 1; w++) {
        if (adjM[v][w] === 0 || dis[w] > -1) continue;
        dis[w] = dis[v] + 1;
        queue.push(w);
      }
    }

    return dis.slice(1).join(" ");
  };

  const answer = [];
  for (const [a, i, j] of plans) {
    adjM[i][j] = 2 - a;
    adjM[j][i] = 2 - a;
    answer.push(bfs());
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
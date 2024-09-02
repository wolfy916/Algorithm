/**
 * 제목 : 트리의 지름
 * 난이도 : 골드 2
 * 분류 : 그래프, 트리
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const V = Number(input[0]);
  const adjL = Array.from(Array(V + 1), () => []);

  let line, j, a, b, c;
  for (let i=1; i<V + 1; i++) {
    line = convert(input[i]);
    j = 0;
    a = line[j++];
    while (line[j] !== -1) {
      b = line[j];
      c = line[j + 1];
      adjL[a].push([b, c]);
      j += 2;
    }
  }

  let startNode = 0, nextNode = 0;
  for (let i=1; i<V+1; i++) {
    if (adjL[i].length === 1) {
      startNode = i;
      break;
    }
  }

  let answer = 0;
  const visited = Array(V + 1).fill(false);
  dfs(startNode, 0, startNode);
  visited.fill(false);
  dfs(nextNode, 0, nextNode);

  return answer;

  function dfs(v, d, s) {
    visited[v] = true;
    if (adjL[v].length === 1 && v !== s) {
      if (answer < d) {
        answer = d;
        nextNode = v;
      }
      return;
    }

    let w, c;
    for (let i=0; i<adjL[v].length; i++) {
      w = adjL[v][i][0];
      if (visited[w]) continue;
      c = adjL[v][i][1];
      dfs(w, d + c, s);
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
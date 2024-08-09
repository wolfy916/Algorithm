/**
 * 제목 : 이분 그래프
 * 난이도 : 골드 4
 * 분류 : 그래프, DFS
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const answer = [];
  let K = Number(input[0]);
  let line = 1;

  while (K--) {
    let [V, E] = convert(input[line++]);
    const adjL = Array.from(Array(V + 1), () => []);

    while (E--) {
      const [u, v] = convert(input[line++]);
      adjL[u].push(v);
      adjL[v].push(u);
    }

    const dfs = (v, flag) => {
      for (const w of adjL[v]) {
        if (visited[w] === 0) {
          visited[w] = flag;
          if (!dfs(w, flag === 1 ? 2 : 1)) {
            return false;
          }
        } else if (visited[w] !== flag) {
          return false;
        }
      }
      return true;
    };

    const visited = Array.from(Array(V + 1), () => 0);
    let isBinaryGraph = "YES";

    for (let v = 1; v < V + 1; v++) {
      if (visited[v]) continue;
      visited[v] = 1;
      if (!dfs(v, 2)) {
        isBinaryGraph = "NO";
        break;
      }
    }

    answer.push(isBinaryGraph);
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
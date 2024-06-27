/**
 * 제목 : BFS 스페셜 저지
 * 난이도 : 골드 3
 * 분류 : BFS, 정렬
 */
const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const N = Number(input[0]);
  const adjL = Array.from({ length: N + 1 }, () => []);
  const answer = convert(input[N]);
  if (answer[0] !== 1) return 0;
  
  for (let i = 1; i < N; i++) {
    const [a, b] = convert(input[i]);
    adjL[a].push(b);
    adjL[b].push(a);
  }

  const priority = new Array(N + 1);
  for (let i = 0; i < N; i++) priority[answer[i]] = i + 1;

  adjL.map((nextNodes) => nextNodes.sort((a, b) => priority[a] - priority[b]));

  return bfs(1);

  function bfs(start) {
    const queue = [];
    const visited = Array.from({ length: N + 1 }, () => false);
    queue.push(start);
    visited[start] = true;
    let head = 0;

    while (queue.length > head) {
      const v = queue[head];
      if (answer[head++] !== v) return 0;
      for (const w of adjL[v]) {
        if (visited[w]) continue;
        visited[w] = true;
        queue.push(w);
      }
    }

    return 1;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
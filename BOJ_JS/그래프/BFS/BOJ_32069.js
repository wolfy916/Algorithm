/**
 * 제목 : 가로등
 * 난이도 : 골드 5
 * 분류 : BFS
 */

const convert = (strArr) => strArr.split(" ").map(v => BigInt(v));

const solution = (input) => {
  let [L, N, K] = convert(input[0]);
  let queue = convert(input[1]);
  
  const visited = new Map();
  queue.forEach(v => visited.set(v, true));
  
  const answer = [];
  let darkness = 0;
  while (queue.length > 0 && K > 0) {
    queue = bfs(queue, darkness++);
  }
  
  return answer.join('\n');

  function bfs(queue, darkness) {
    const nxtQueue = [];
    for (const v of queue) {
      if (K-- < 1) break;
      answer.push(darkness);
      for (const w of [v - BigInt(1), v + BigInt(1)]) {
        if (w < 0 || w > L) continue;
        if (visited.get(w)) continue;
        visited.set(w, true);
        nxtQueue.push(w);
      }
    }
    return nxtQueue;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
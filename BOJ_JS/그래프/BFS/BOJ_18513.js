/**
 * 제목 : 샘터
 * 난이도 : 골드 4
 * 분류 : BFS
 * 
 * BFS라고 떠올리기 쉽지 않음..
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, K] = convert(input[0]);
  let queue = input[1].split(" ").map(Number);

  const visited = new Map();
  for (let i = 0; i < N; i++) {
    visited.set(queue[i], true);
  }

  let answer = 0;
  let cnt = 0;
  let d = 1;

  while (queue.length > 0) {
    const nxtQueue = [];
    let p = 0;

    while (p < queue.length) {
      const v = queue[p++];
      for (const w of [v - 1, v + 1]) {
        if (visited.get(w)) continue;
        answer += d;
        cnt++;
        if (cnt >= K) return answer;
        visited.set(w, true);
        nxtQueue.push(w);
      }
    }

    queue = nxtQueue;
    d++;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
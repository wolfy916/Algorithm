/**
 * 제목 : 숨바꼭질 2
 * 난이도 : 골드 4
 * 분류 : bfs, deque
 */

const deque = () => {
  const ref = new Map();
  let idx = 0;
  let head = 0;

  const push = (x) => {
    ref.set(idx++, x);
  }

  const shift = () => {
    if (idx - head <= 0) return null;
    const shiftData = ref.get(head);
    ref.delete(head++);
    return shiftData;
  }

  const size = () => idx - head;

  return {
    push,
    shift,
    size,
  };
}

const solution = (input) => {
  const [N, K] = input[0].split(" ").map(Number);

  const answer = [0, 0];
  
  const bfs = () => {
    const visited = Array.from({ length: 100001 }, () => Infinity);
    visited[N] = 0;
    const queue = deque();
    queue.push([N, 0]);
    while (queue.size() > 0) {
      const [v, t] = queue.shift();
      if (v === K) {
        answer[0] = visited[K];
        answer[1]++;
        continue;
      }
      for (const w of [v - 1, v + 1, v * 2]) {
        if (w < 0 || w > 100000) continue;
        if (visited[w] < t + 1) continue;
        if (answer[0] > 0 && answer[0] < t + 1) continue;
        visited[w] = t + 1;
        queue.push([w, t + 1]);
      }
    }
    answer[0] = visited[K];
  }

  bfs();

  return answer.join('\n');
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
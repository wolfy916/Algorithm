/**
 * 제목 : 1로 만들기 2
 * 난이도 : 실버 1
 * 분류 : 다이나믹 프로그래밍, 그래프 탐색
 */

const solution = (input) => {
  const N = Number(input[0]);
  const f = [
    (x) => x / 3,
    (x) => x / 2,
    (x) => x - 1,
  ];
  const isValid = [
    (x) => x % 3 === 0,
    (x) => x % 2 === 0,
    () => true,
  ]
  const visited = new Array(N + 1).fill(false);
  let answer = [];

  bfs(N);

  answer.sort((a, b) => a.count - b.count);

  return answer[0].count + "\n" + answer[0].log;

  function bfs(x) {
    const queue = [{
      value: x,
      count: 0,
      log: x,
    }];
    let nxtValue, head = 0;
    while (head < queue.length) {
      const { value, count, log } = queue[head++];
      if (value === 1) {
        answer.push(queue[head - 1]);
        return;
      }
      if (visited[value] || value < 1) continue;
      visited[value] = true;
      for (let i=0; i<3; i++) {
        if (!isValid[i](value)) continue;
        nxtValue = f[i](value);
        if (visited[nxtValue]) continue;
        queue.push({
          value: nxtValue,
          count: count + 1,
          log: log + " " + nxtValue,
        })
      }
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 괄호 추가하기
 * 난이도 : 골드 5
 * 분류 : 브루트-포스, 구현
 */

const solution = (input) => {
  const N = Number(input[0]);
  const formula = input[1].split("").map(v => isNaN(v) ? v : Number(v));
  const calculation = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
  }

  let answer = -Infinity;
  const visited = Array(N).fill(false);
  dfs(1, [formula[0]]);

  return answer;

  function dfs(idx, queue) {
    if (idx > N - 2) {
      let result = queue[0];
      let num;
      const tmp = [];
      for (let i=1; i<queue.length; i++) {
        num = queue[i];
        for (let j=1; j<N; j += 2) {
          if (visited[j]) continue;
          visited[j] = true;
          result = calculation[formula[j]](result, num);
          tmp.push(j);
          break;
        }
      }
      answer = Math.max(answer, result);
      tmp.forEach((v) => visited[v] = false);
      return;
    }

    // 계산안함
    queue.push(formula[idx + 1]);
    dfs(idx + 2, queue);
    queue.pop();

    // 계산함
    if (visited[idx - 2] === false) {
      queue[queue.length - 1] = calculation[formula[idx]](queue[queue.length - 1], formula[idx + 1]);
      visited[idx] = true;
      dfs(idx + 2, queue);
      visited[idx] = false;
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
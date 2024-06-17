/**
 * 제목 : 숫자 고르기
 * 난이도 : 골드 5
 * 분류 : dfs
 */

const solution = (input) => {
  const N = +input[0];
  const nums = input.slice(1).map(Number);
  const answer = [];
  const visited = Array.from({ length: N + 1 }, () => 0);

  for (let i=1; i<N + 1; i++) {
    if (i === nums[i - 1]) {
      visited[i] = i;
      answer.push(i);
    }
  }

  const dfs = (curNum, startNum) => {
    const nextNum = nums[curNum - 1];
    if (nextNum === startNum) return true;

    if (visited[nextNum] === 0) {
      visited[nextNum] = startNum;
      if (dfs(nextNum, startNum)) return true;
      visited[nextNum] = 0;
    }

    return false;
  }

  for (let i=1; i<N+1; i++) {
    if (visited[i]) continue;
    visited[i] = i;
    if (dfs(i, i)) {
      for (let j=1; j<N + 1; j++) {
        if (visited[j] === i) answer.push(j);
      }
    }
  }

  answer.sort((a, b) => a - b);

  return answer.length + '\n' + answer.join('\n');
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
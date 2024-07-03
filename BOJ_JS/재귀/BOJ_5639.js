/**
 * 제목 : 이진 검색 트리
 * 난이도 : 골드 4
 * 분류 : 재귀, 트리
 */

const solution = (input) => {
  const arr = input.map(Number);
  const answer = [];

  dfs(0, arr.length);

  return answer.join('\n');

  function dfs(p1, p2) {
    if (p2 - p1 === 0) return;

    const mid = arr[p1];
    let nxt = p2;

    for (let i=p1; i<p2; i++) {
      if (mid < arr[i]) {
        nxt = i;
        break;
      }
    }

    dfs(p1 + 1, nxt);
    dfs(nxt, p2);
    answer.push(mid);
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
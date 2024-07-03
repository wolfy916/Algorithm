/**
 * 제목 : A와 B 2
 * 난이도 : 골드 5
 * 분류 : 재귀, 문자열, 브루트포스
 */

const solution = (input) => {
  const S = input[0].trim();
  const T = input[1].trim();
  let answer = 0;

  dfs(T);

  return answer;

  function dfs(t) {
    if (T.length < 1 || answer === 1) return;
    if (t === S) {
      answer = 1;
      return;
    }
    if (t[t.length - 1] === 'A') dfs(t.slice(0, t.length - 1));
    if (t[0] === 'B') dfs(t.split('').slice(1,).reverse().join(''));
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
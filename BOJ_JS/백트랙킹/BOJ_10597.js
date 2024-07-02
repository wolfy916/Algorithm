/**
 * 제목 : 순열장난
 * 난이도 : 골드 5
 * 분류 : 백트랙킹
 */

const solution = (input) => {
  const len = input.length;
  const completed = Array.from({ length : 51 }, () => false);
  let answer = undefined;

  dfs(0, []);
  
  return answer.join(' ');

  function check(N) {
    for (let i=1; i<N + 1; i++) {
      if (!completed[i]) return false;
    }
    return true;
  }

  function dfs(i, arr) {
    // input 순회 완료시
    if (i >= len) {
      if (check(arr.length)) {
        answer = arr;
        return true;
      } else return false;
    }

    // 한 글자
    if (input[i] !== '0') {
      const num = Number(input[i]);
      if (!completed[num]) {
        completed[num] = true;
        arr.push(num);
        if (dfs(i + 1, arr)) return true;
        completed[num] = false;
        arr.pop();
      }
    }

    // 두 글자
    if (input[i] !== '0' && i + 1 < len) {
      const num = Number(input.slice(i, i + 2));
      if (!completed[num]) {
        completed[num] = true;
        arr.push(num);
        if (dfs(i + 2, arr)) return true;
        completed[num] = false;
        arr.pop();
      }
    }
    
    return false;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();
console.log(solution(input));
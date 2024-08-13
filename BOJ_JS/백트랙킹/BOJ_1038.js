/**
 * 제목 : 감소하는 수
 * 난이도 : 골드 5
 * 분류 : 조합, 백트랙킹
 */

const solution = (input) => {
  const N = Number(input);
  const numbers = [];
  
  let combinations;
  for (let i=1; i<11; i++) {
    combinations = [];
    getCombination([], i, 0);
    for (const c of combinations) {
       numbers.push(c.reverse().join(""));
    }
  }

  numbers.sort((a, b) => a - b);
  
  return N >= numbers.length ? -1 : numbers[N];

  function getCombination(arr, count, s) {
    if (count === 0) {
      combinations.push([...arr]);
      return;
    }

    for (let i=s; i<10; i++) {
      arr.push(i);
      getCombination(arr, count - 1, i + 1);
      arr.pop();
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();
console.log(solution(input));
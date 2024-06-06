/**
 * 제목 : 카드 숫자 곱을 최소로 만들기
 * 난이도 : 실버 1
 * 분류 : 백트랙킹
 */

const solution = (input) => {
  const [n, nums] = [+input[0], input[1].split(" ").map(Number)];

  const pA = nums.reduce((acc, cur) => acc * cur, 1);
  if (pA >= Math.pow(9, n)) return -1;

  const answer = [];
  const dfs = (value) => {
    if (answer.length >= n) return value > pA ? true : false;

    for (let num=1; num<10; num++) {
      answer.push(num);
      const flag = dfs(value * num);
      if (flag) return true;
      answer.pop();
    }

    return false;
  }
  
  dfs(1);

  return answer.sort((a, b) => a - b).join(" ");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
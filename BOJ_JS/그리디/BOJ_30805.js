/**
 * 제목 : 사전 순 최대 공통 부분 수열
 * 난이도 : 골드 4
 * 분류 : 그리디
 */

// 와 그리디 진짜 어렵다..

const solution = (input) => {
  const convert = s => s.split(" ").map(Number);
  const N = Number(input[0]);
  const A = convert(input[1]);
  const M = Number(input[2]);
  const B = convert(input[3]);
  const answer = search(A, B);

  return `${answer.length}\n${answer.join(" ")}`

  function search(a, b, res = []) {
    if (a.length === 0 || b.length === 0) return res;

    const maxA = Math.max(...a);
    const maxB = Math.max(...b);
    const maxAIdx = a.indexOf(maxA);
    const maxBIdx = b.indexOf(maxB);

    if (maxA === maxB) {
      res.push(maxA);
      return search(a.slice(maxAIdx + 1,), b.slice(maxBIdx + 1,), res);
    } else if (maxA > maxB) {
      return search([...a.slice(0, maxAIdx), ...a.slice(maxAIdx + 1,)], b, res);
    } else {
      return search(a, [...b.slice(0, maxBIdx), ...b.slice(maxBIdx + 1,)], res);
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
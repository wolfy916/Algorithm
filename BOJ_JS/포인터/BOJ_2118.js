/**
 * 제목 : 두 개의 탑
 * 난이도 : 골드 5
 * 분류 : 누적합, 투 포인터
 */

const solution = (input) => {
  const N = Number(input[0]);
  const d = input.slice(1,).map(Number);
  const totalD = d.reduce((a, c) => a + c);

  let answer = 0;
  let [p1, p2] = [0, 0];
  let sumD = 0;
  while (p1 < N - 1) {
    while (p2 < N - 1 && sumD < Math.floor(totalD / 2) + 1) {
      sumD += d[p2++];
      answer = Math.max(answer, getMinD(sumD));
    }
    sumD -= d[p1++];
    answer = Math.max(answer, getMinD(sumD));
  }

  return answer;

  function getMinD(sumD) {
    return Math.min(sumD, totalD - sumD);
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
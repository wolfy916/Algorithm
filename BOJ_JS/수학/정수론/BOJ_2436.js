/**
 * 제목 : 공약수
 * 난이도 : 골드 5
 * 분류 : 수학(정수론)
 */

const solution = (input) => {
  const [A, B] = input[0].split(" ").map(Number);
  if (A === B) return A + " " + B;
  const tmp = B / A;
  const answer = [];

  for (let a = 1; a < Math.ceil(Math.sqrt(tmp)); a++) {
    if (tmp % a === 0 && getGCD(a, tmp / a) === 1) {
      answer.push([A * a, (A * tmp) / a]);
    }
  }

  answer.sort((a, b) => a[0] + a[1] - b[0] - b[1]);

  return answer[0].join(" ");

  function getGCD(a, b) {
    return a % b ? getGCD(b, a % b) : b;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
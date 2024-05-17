/**
 * 제목 : 콘센트
 * 난이도 : 골드5
 * 분류 : 그리디
 */

const solution = (input) => {
  const [[_, M], machines] = input.map((v) => v.split(" ").map((v) => +v));
  machines.sort((a, b) => a - b);
  let answer = 0;
  let waste;
  let sockets = [];
  while (machines.length > 0 || sockets.length > 0) {
    if (sockets.length < M && machines.length > 0) {
      sockets.push(machines.pop());
      sockets.sort((a, b) => b - a);
    } else {
      waste = sockets.pop();
      sockets = sockets.map(v => v - waste);
      while (sockets.length > 0 && sockets[sockets.length - 1] <= 0) {
        sockets.pop();
      }
      answer += waste;
    }
  }
  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
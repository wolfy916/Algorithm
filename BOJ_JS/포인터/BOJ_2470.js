/**
 * 제목 : 두 용액
 * 난이도 : 골드 5
 * 분류 : 투 포인터
 */

const solution = (input) => {
  const N = Number(input[0]);
  const arr = input[1].split(" ").map(Number);

  arr.sort((a, b) => a - b);

  let [p1, p2] = [0, N - 1];
  let sumV = Math.abs(arr[p1] + arr[p2]);
  const answer = [arr[p1], arr[p2]];
  while (p1 < p2) {
    const sum = arr[p1] + arr[p2];
    if (Math.abs(sum) < sumV) {
      sumV = Math.abs(sum);
      answer[0] = arr[p1];
      answer[1] = arr[p2];
    }
    if (sum < 0) {
      p1++;
    } else if (0 < sum) {
      p2--;
    } else break;
  }

  return answer.join(" ");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
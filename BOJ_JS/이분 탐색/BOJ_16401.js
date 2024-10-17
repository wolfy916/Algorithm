/**
 * 제목 : 과자 나눠주기
 * 난이도 : 실버 2
 * 분류 : 이분 탐색
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [M, N] = convert(input[0]);
  const snacks = convert(input[1]);

  const check = (mid) => {
    let count = 0;
    for (let i=0; i<N; i++) {
      count += Math.floor(snacks[i] / mid);
    }
    return count >= M;
  }

  let mid, [left, right] = [0, 1e9], answer = 0;
  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    if (check(mid)) {
      answer = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  
  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
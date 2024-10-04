/**
 * 제목 : 소수 구하기
 * 난이도 : 실버 3
 * 분류 : 수학(소수), 아리스토테네스의 체
 */

const solution = (input) => {
  const [M, N] = input[0].split(" ").map(Number);
  const arr = Array.from({ length: N + 1 }, (_, i) => true);
  const answer = [];

  arr[1] = false;

  for (let i = 2; i < N + 1; i++) {
    if (!arr[i]) continue;
    for (let j = i * 2; j < N + 1; j += i) {
      arr[j] = false;
    }
  }

  for (let i = M; i < N + 1; i++) {
    if (arr[i]) answer.push(i);
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
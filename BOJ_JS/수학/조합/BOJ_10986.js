/**
 * 제목 : 나머지 합
 * 난이도 : 골드 3
 * 분류 : 수학, 누적합
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const [N, M] = convert(input[0]);
  const A = convert(input[1]);

  // 1차원 누적합
  for (let i = 1; i < N; i++) {
    A[i] += A[i - 1];
  }

  // M으로 나눈 나머지 값을 카운트
  const count = Array(M).fill(0);
  for (let i = 0; i < N; i++) {
    A[i] %= M;
    count[A[i]]++;
  }

  // 카운트값에서 2개를 선택하는 조합의 수를 합산
  let answer = count[0]; // default
  for (let i = 0; i < M; i++) {
    answer += (count[i] * (count[i] - 1)) / 2;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 태상이의 훈련소 생활
 * 난이도 : 골드 5
 * 분류 : 누적합
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  // 데이터 입력 및 초기화
  const [N, _] = convert(input[0]);
  const heights = convert(input[1]);
  const infos = input.slice(2,).map(convert);
  const prefixSum = Array.from({ length: N + 2 }, () => 0);

  // 누적합 연산 표기
  for (const [a, b, k] of infos) {
    prefixSum[a] += k;
    prefixSum[b + 1] -= k;
  }

  // 누적합 연산 진행
  for (let i=1; i<N + 1; i++) {
    prefixSum[i] += prefixSum[i - 1];
  }

  // 누적합 결과 반영
  for (let i=0; i<N; i++) {
    heights[i] += prefixSum[i + 1];
  }

  return heights.join(" ");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
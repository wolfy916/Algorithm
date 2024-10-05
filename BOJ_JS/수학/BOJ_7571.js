/**
 * 제목 : 점 모으기
 * 난이도 : 실버 1
 * 분류 : 수학(중앙값), 정렬
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const [N, M] = convert(input[0]);
  const R = [];
  const C = [];

  let r, c;
  for (let i=1; i<M + 1; i++) {
    [r, c] = convert(input[i]);
    R.push(r);
    C.push(c);
  }

  R.sort((a, b) => a - b);
  C.sort((a, b) => a - b);

  let mr = R[Math.floor(M / 2)];
  let mc = C[Math.floor(M / 2)];

  if (M % 2 === 0) {
    mr = (mr + R[Math.floor(M / 2) - 1]) / 2;
    mc = (mc + C[Math.floor(M / 2) - 1]) / 2;
  }

  let answer = 0;
  for (let i=0; i<M; i++) {
    answer += Math.abs(mr - R[i]);
    answer += Math.abs(mc - C[i]);
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
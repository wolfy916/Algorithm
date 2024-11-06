/**
 * 제목 : 디버깅
 * 난이도 : 골드 3
 * 분류 : 투 포인터
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M] = convert(input[0]);
  const errors = convert(input[1]);
  const [X, Y] = convert(input[2]);
  const isError = Array(N + 1).fill(0);

  for (let i=0; i<M; i++) {
    isError[errors[i]] = 1;
  }

  let [p1, p2] = [1, 1];
  let errorCount = 0;
  let term = 0;
  let minErrorCount = Infinity;

  if (N === 1) return M - Y;

  while (p1 < N) {
    if ((errorCount < Y || term < X) && p2 <= N) {
      if (isError[p2++]) errorCount++;
      term++;
    } else {
      if (errorCount >= Y && term >= X) minErrorCount = Math.min(minErrorCount, errorCount);
      if (isError[p1++]) errorCount--;
      term--;
    }
  }

  const answer = M - minErrorCount;

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
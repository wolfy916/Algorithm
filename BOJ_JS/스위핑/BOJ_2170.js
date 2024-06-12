/**
 * 제목 : 선 긋기
 * 난이도 : 골드 5
 * 분류 : 스위핑, 정렬
 */

const solution = (input) => {
  const N = Number(input[0]);
  const lines = input.slice(1,).map(v => v.split(" ").map(Number));

  lines.sort((a, b) => a[0] - b[0]);

  let [s, e] = lines[0];
  let answer = e - s;

  for (let i=1; i<N; i++) {
    if (lines[i][1] <= e) continue;
    if (lines[i][0] <= e) {
      answer += lines[i][1] - e;
      e = lines[i][1];
    } else {
      answer += lines[i][1] - lines[i][0];
      s = lines[i][0];
      e = lines[i][1];
    }
  }

  return answer;
};

const fs = require('fs');
const filePath = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split('\n');
console.log(solution(input));
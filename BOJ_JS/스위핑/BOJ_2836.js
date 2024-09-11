/**
 * 제목 : 수상 택시
 * 난이도 : 골드 3
 * 분류 : 스위핑, 정렬
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const [N, M] = convert(input[0]);
  const info = input.slice(1,).map(convert).filter(v => v[0] > v[1]);

  if (N < 1 || info.length === 0) return M;

  info.sort((a, b) => {
    if (a[0] === b[0]) return a[1] - b[1];
    else return b[0] - a[0];
  });

  let answer = M;
  let [s, e] = [info[0][0], info[0][1]];
  for (let i=1; i<info.length; i++) {
    if (info[i][0] === s || info[i][1] >= e) continue;
    if (info[i][0] >= e && info[i][1] < e) {
      e = info[i][1];
    } else {
      answer += (s - e) * 2;
      s = info[i][0];
      e = info[i][1];
    }
  }

  answer += (s - e) * 2;

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
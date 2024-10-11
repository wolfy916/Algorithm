/**
 * 제목 : 부분수열의 합
 * 난이도 : 실버 2
 * 분류 : 백트랙킹
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, S] = convert(input[0]);
  const arr = convert(input[1]);

  const count = (idx, sumV) => {
    if (idx >= N) return 0;
    sumV += arr[idx];
    let cnt = sumV === S ? 1 : 0;
    cnt += count(idx + 1, sumV);
    sumV -= arr[idx];
    cnt += count(idx + 1, sumV);
    return cnt;
  };

  return count(0, 0);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
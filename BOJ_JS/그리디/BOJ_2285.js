/**
 * 제목 : 우체국
 * 난이도 : 골드 4
 * 분류 : 그리디, 정렬
 */

const solution = (input) => {
  const N = Number(input[0]);
  const arr = Array.from(Array(N), () => Array(2));
  
  let total = 0;
  for (let i = 0; i < N; i++) {
    const [x, a] = input[i + 1].split(" ").map(Number);
    arr[i][0] = x;
    arr[i][1] = a;
    total += a;
  }

  arr.sort((a, b) => a[0] - b[0]);
  
  const target = total / 2;
  let sumV = 0;
  for (let i = 0; i < N; i++) {
    sumV += arr[i][1];
    if (sumV < target) continue;
    answer = arr[i][0];
    break;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
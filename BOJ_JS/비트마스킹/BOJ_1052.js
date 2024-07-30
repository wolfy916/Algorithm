/**
 * 제목 : 물병
 * 난이도 : 골드 5
 * 분류 : 비트마스킹, 그리디
 */

const solution = (input) => {
  const [N, K] = input[0].split(" ").map(Number);
  if (N <= K) return 0;
  
  const bit = []; // 비트의 인덱스를 담을 배열
  const bin = N.toString(2); // 이진 비트열

  // 비트 인덱스 담기
  bin.split("").forEach((v, i) => {
    if (v === '1') bit.push(bin.length - i - 1);
  });
  // K가 비트 인덱스 개수이상이면 0
  if (bit.length <= K) return 0;

  // 필요한 만큼 이진수를 더하며, 비트 수 줄이기
  let answer = 0;
  while (bit.length !== K) {
    const bitIdx = bit.pop();
    if (bitIdx !== bit[bit.length - 1]) {
      answer += Math.pow(2, bit[bit.length - 1]) - Math.pow(2, bitIdx);
    }
    bit[bit.length - 1]++;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
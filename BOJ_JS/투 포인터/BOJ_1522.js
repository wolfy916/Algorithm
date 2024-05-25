/**
 * 제목 : 문자열 교환
 * 난이도 : 실버 1
 * 분류 : 투 포인터, 윈도우 슬라이딩
 */

/**
 * 접근 방식
 * b의 총 개수를 길이로 윈도우 슬라이딩
 */

const solution = (input) => {
  const N = input.length;

  // b 개수 카운팅
  let totalB = input.split("a").length;
  if (totalB < 2) return 0;

  // 윈도우의 a 개수 카운팅
  let countA = 0;
  for (let i=0; i<totalB; i++) {
    if (input[i] === 'a') countA++;
  }

  // 투 포인터로 윈도우 슬라이딩 진행하며 answer값 갱신
  let answer = 1001;
  let [p1, p2] = [0, totalB - 1];
  while (true) {
    answer = Math.min(answer, countA);
    if (input[p1] === 'a') countA--;
    p1 = (p1 + 1) % N;
    p2 = (p2 + 1) % N;
    if (input[p2] === 'a') countA++;
    if (p2 === totalB - 1) break;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim();
console.log(solution(inputArr));
/**
 * 제목 : 회전 초밥
 * 난이도 : 실버 1
 * 분류 : 투 포인터, 슬라이딩 윈도우
 */

const solution = (input) => {
  const [N, d, k, c] = input[0].split(" ").map(Number);
  const sushi = Array.from(Array(N + k - 1), () => 0);
  
  for (let i=0; i<N; i++) {
    sushi[i] = Number(input[i + 1]);
  }

  for (let i=N; i<N + k - 1; i++) {
    sushi[i] = sushi[i - N];
  }

  const isSelected = Array.from(Array(d + 1), () => 0);
  let count = 0;
  let answer = 0;

  for (let i=0; i<k; i++) {
    if (isSelected[sushi[i]] === 0) count++;
    isSelected[sushi[i]]++;
  }

  let [p1, p2] = [0, k];
  while (p2 <= sushi.length) {
    answer = Math.max(answer, isSelected[c] ? count : count + 1);
    if (isSelected[sushi[p1]] === 1) count--;
    isSelected[sushi[p1++]]--;
    if (isSelected[sushi[p2]] === 0) count++;
    isSelected[sushi[p2++]]++;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
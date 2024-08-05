/**
 * 제목 : 과일 탕후루
 * 난이도 : 실버 2
 * 분류 : 투 포인터
 */

const solution = (input) => {
  const N = Number(input[0]);
  const fruits = input[1].split(" ").map(Number);
  const count = Array(10).fill(0);

  let answer = 0;
  let [p1, p2] = [0, 0];
  while (p2 < N) {

    while (p2 - p1 <= answer) {
      count[fruits[p2++]]++;
    }

    if (check()) {
      answer = Math.max(answer, p2 - p1);
    } else {
      count[fruits[p1++]]--;
    }
  }

  return answer;

  function check() {
    let fruitCount = 0;
    for (let i=1; i<10; i++) {
      if (count[i] === 0) continue;
      if (++fruitCount > 2) return false;
    }
    return true;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
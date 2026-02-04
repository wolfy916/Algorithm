/**
 * 제목 : 준표의 조약돌
 * 난이도 : 골드 4
 * 분류 : 투 포인터
 */

const solution = (input) => {
  const [n, b, w] = input[0].split(" ").map(Number);
  const str = input[1].trim();

  const count = { B: 0, W: 0 };
  let maxLength = 0;
  let p1 = 0;

  for (let p2 = 0; p2 < n; p2++) {
    count[str[p2]]++;

    while (count.B > b) {
      count[str[p1]]--;
      p1++;
    }

    if (count.W >= w) {
      maxLength = Math.max(maxLength, p2 - p1 + 1);
    }
  }

  return maxLength;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 색칠 1
 * 난이도 : 골드 5
 * 분류 : 구현
 */

const solution = (input) => {
  let [W, H, f, c, x1, y1, x2, y2] = input.map(BigInt);
  
  x1 += f; x2 += f;

  let tmpX = f;
  if (f <= W - f) tmpX += f;
  else tmpX += W - f;

  let answer = W * H;

  let aWidth = BigInt(0);
  if (x1 < tmpX) {
    if (x2 <= tmpX) {
      aWidth = (x2 <= tmpX ? x2 : tmpX) - x1;
    } else {
      aWidth = tmpX - x1;
    }
  }

  answer -= (c + BigInt(1)) * BigInt(2) * aWidth * (y2 - y1);

  let bWidth = BigInt(0);
  if (tmpX < x2) {
    if (tmpX <= x1) {
      bWidth = x2 - (tmpX <= x1 ? x1 : tmpX);
    } else {
      bWidth = x2 - tmpX;
    }
  }

  answer -= (c + BigInt(1)) * bWidth * (y2 - y1);

  return answer.toString();
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split(" ");
console.log(solution(inputArr));
/**
 * 제목 : K진 트리
 * 난이도 : 골드 3
 * 분류 : 트리
 */

const solution = (input) => {
  const [N, K, Q] = input[0].split(" ").map(Number);
  const couples = Array.from({ length: Q }, (_, i) => {
    return input[i + 1].split(" ").map(v => Number(v) - 1);
  });

  const getPar = (x) => Math.floor((x - 1) / K);
  const getDepth = (x) => {}
  
  const answer = [];
  const count = new Map();
  let bigNumber, smallNumber;
  
  for (const [x, y] of couples) {
    count.clear();

    smallNumber = Math.max(x, y);
    bigNumber = Math.max(x, y);

    count.set(smallNumber, 0);

    let par;
    while(smallNumber > 0) {
      par = getPar(smallNumber);
      count.set(par, count.get(smallNumber) + 1);
      smallNumber = par;
    }

    let distance = 1;
    while (bigNumber > 0) {
      par = getPar(bigNumber);
      if (count.get(par)) {
        
      } else {

      }
    }
  }



  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
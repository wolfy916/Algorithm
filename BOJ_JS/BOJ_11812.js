/**
 * 제목 : K진 트리
 * 난이도 : 골드 3
 * 분류 : 트리, 최소 공통 조상
 */

const solution = (input) => {
  const [_, K, Q] = input[0].split(" ").map(Number);
  const couples = Array.from({ length: Q }, (_, i) => {
    return input[i + 1].split(" ").map((v) => Number(v) - 1);
  });

  const getPar = (x) => Math.floor((x - 1) / K);
  const getDepth = (x) => {
    let depth = 1;
    while (x > 0) {
      x = getPar(x);
      depth++;
    }
    return depth;
  };

  const answer = [];

  let bigNumber, smallNumber;
  let bigNumberDepth, smallNumberDepth;
  let bigNumberCount, smallNumberCount;

  for (const [x, y] of couples) {
    smallNumber = Math.min(x, y);
    bigNumber = Math.max(x, y);

    smallNumberDepth = getDepth(smallNumber);
    bigNumberDepth = getDepth(bigNumber);

    smallNumberCount = 0;
    bigNumberCount = 0;

    while (smallNumberDepth < bigNumberDepth) {
      bigNumber = getPar(bigNumber);
      bigNumberDepth--;
      bigNumberCount++;
    }

    while (smallNumber !== bigNumber) {
      smallNumber = getPar(smallNumber);
      smallNumberCount++;

      bigNumber = getPar(bigNumber);
      bigNumberCount++;
    }

    answer.push(smallNumberCount + bigNumberCount);
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
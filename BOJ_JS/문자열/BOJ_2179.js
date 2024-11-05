/**
 * 제목 : 비슷한 단어
 * 난이도 : 골드 4
 * 분류 : 문자열, 해시를 사용한 집합과 맵
 */

const solution = (input) => {
  const N = Number(input.shift());
  const answerWordIndex = [0, 1];
  const index = {};
  let maxCount = 0;

  input = input.map((v) => v.trim());

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < input[i].length; j++) {
      const prefix = input[i].slice(0, j + 1);
      if (index[prefix] !== undefined) {
        if (index[prefix] === i) continue;
        if (input[index[prefix]] === input[i]) continue;

        if (prefix.length === maxCount) {
          if (answerWordIndex[0] > index[prefix]) {
            answerWordIndex[0] = index[prefix];
            answerWordIndex[1] = i;
          }
        } else if (prefix.length > maxCount) {
          answerWordIndex[0] = index[prefix];
          answerWordIndex[1] = i;
          maxCount = prefix.length;
        }
      } else {
        index[prefix] = i;
      }
    }
  }

  return answerWordIndex.map((v) => input[v]).join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
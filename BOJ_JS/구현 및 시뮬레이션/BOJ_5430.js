/**
 * 제목 : AC
 * 난이도 : 골드5
 * 분류 : 구현, 파싱
 */

const solution = (input) => {
  const T = +input[0];
  const answer = [];
  let line = 0;

  for (let tc=0; tc<T; tc++) {
    const [p, n, arr] = [
      input[++line].trim(),
      +input[++line],
      JSON.parse(input[++line])
    ];

    let isError = false;
    let [head, tail, isReversed] = [0, n - 1, false];
    for (const func of p) {
      if (func === 'R') {
        isReversed = !isReversed;
      } else if (func === 'D') {
        if (head > tail) {
          isError = true;
          break;
        }
        if (isReversed) tail--;
        else head++;
      }
    }

    let result = arr.slice(head, tail + 1);
    if (isReversed) result = result.reverse();
    answer.push(isError ? "error" : JSON.stringify(result));
  }

  return answer.join('\n');
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
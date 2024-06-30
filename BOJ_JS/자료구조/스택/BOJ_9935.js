/**
 * 제목 : 문자열 폭발
 * 난이도 : 골드 4
 * 분류 : 문자열, 스택
 */

// stack의 문자열을 join해서 폭탄 문자열과 전체를 비교하고,
// slice를 사용해서 stack에 재할당하니 메모리 초과

const solution = (input) => {
  const stack = [];
  for (const char of input[0]) {
    // push
    stack.push(char);

    // stack 길이가 폭탄 문자열의 길이 이상이라면
    // 최근 push한 부분에서 폭탄이 포함되어있는지 확인
    if (input[1].length <= stack.length) {
      let isValid = true;
      const startIdx = stack.length - input[1].length;
      for (let i=0; i<input[1].length; i++) {
        if (stack[startIdx + i] !== input[1][i]) {
          isValid = false;
          break;
        }
      }

      // 폭탄을 확인하면 pop
      if (isValid) {
        let cnt = input[1].length;
        while (cnt-- > 0) stack.pop();
      }
    }
  }

  return stack.length > 0 ? stack.join("") : "FRULA";
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n").map(v => v.trim());

console.log(solution(input));
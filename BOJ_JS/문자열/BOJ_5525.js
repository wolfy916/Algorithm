/**
 * 제목 : IOIOI
 * 난이도 : 실버 1
 * 분류 : 문자열
 */

const solution = (input) => {
  const N = Number(input[0]);
  const M = Number(input[1]);
  const S = input[2].trim();
  const count = { 'I': 0, 'O': 0 };

  let answer = 0;
  count[S[0]]++;
  
  for (let i=1; i<M; i++) {
    if (S[i] === S[i - 1]) {
      count['I'] = 0;
      count['O'] = 0;
      count[S[i]]++;
    } else {
      count[S[i]]++;
      if (count['I'] >= N + 1 && count['O'] >= N) {
        answer++;
        count['I']--;
        count['O']--;
      }
    }
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : ChatGPT 만들기
 * 난이도 : 골드 3
 * 분류 : 구현
 */

const solution = (input) => {
  const [[_, K, M], sentences] = [
    input[0].split(" ").map((v, i) => i === 1 ? BigInt(v) : Number(v)),
    input.slice(1,).map(v => v.trim())
  ]

  let model = {};
  for (let sentence of sentences) {
    for (let i=0; i<sentence.length - 1; i++) {
      if (sentence[i] in model) {
        if (sentence[i + 1] in model[sentence[i]]) {
          model[sentence[i]][sentence[i + 1]]++;
        } else {
          model[sentence[i]][sentence[i + 1]] = 1;
        }
      } else {
        model[sentence[i]] = {};
        model[sentence[i]][sentence[i + 1]] = 1;
      }
    }
  }

  for (let char of Object.keys(model)) {
    let value = '';
    let cnt = 0;
    for (let nxtChar of Object.keys(model[char])) {
      if (model[char][nxtChar] === cnt) {
        value = value.charCodeAt() > nxtChar.charCodeAt() ? nxtChar : value;
      } else if (model[char][nxtChar] > cnt) {
        value = nxtChar;
        cnt = model[char][nxtChar];
      }
    }
    model[char] = [value, -1];
  }

  const word = [];
  let repeat = [0, 0];
  let genChar = '[';
  let k = 0;
  while (k < K + BigInt(M) - BigInt(1)) {
    if (genChar === ']') {
      word.push(genChar);
      break;
    };
    if (model[genChar][1] > -1) {
      repeat = [model[genChar][1], k];
      break;
    } else {
      model[genChar][1] = k;
    }
    word.push(genChar);
    genChar = model[genChar][0];
    k++;
  }

  const repeatWord = word.slice(repeat[0], repeat[1]);
  const repeatLen = repeatWord.length;
  if (repeatLen > 0) {
    let moveWindowCnt = (K - BigInt(repeat[0]) - BigInt(1)) % BigInt(repeatLen);
    while (moveWindowCnt-- > 0) {
      repeatWord.push(repeatWord.shift());
    }
  }

  let answer = word.length >= K ? word.slice(Number(K) - 1,).join("") : "";

  let addWord = '';
  if (repeatLen > 0) {
    const emptySpace = M - answer.length;
    const iter = Math.floor(emptySpace / repeatLen);
    const rest = emptySpace % repeatLen;
    answer += repeatWord.join('').repeat(iter) + repeatWord.slice(0, rest).join('');
  }

  const dots = '.'.repeat(M - answer.length);

  return answer + addWord + dots;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
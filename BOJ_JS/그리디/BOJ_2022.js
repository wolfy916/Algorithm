/**
 * 제목 : 단어 수학
 * 난이도 : 골드 4
 * 분류 : 그리디(가중치 정렬)
 */

// 백트랙킹 완전탐색 풀이 -> 시간초과
const solution1 = (input) => {
  const words = input.slice(1,).map(v => v.trim());
  const isUsed = Array.from({ length: 10 }, () => false);
  const charConvert = new Map();

  for (const word of words) {
    for (const char of word) {
      charConvert.set(char, -1);
    }
  }

  const charKeys = Array.from(charConvert.keys());
  let answer = 0;

  dfs(0);

  return answer;

  function calculate() {
    let sumV = 0;

    for (const word of words) {
      for (let i=0; i<word.length; i++) {
        const char = word[word.length - i - 1];
        sumV += Math.pow(10, i) * charConvert.get(char);
      }
    }

    return sumV;
  }

  function dfs(idx) {
    if (charKeys.length <= idx) {
      answer = Math.max(answer, calculate());
      return;
    }

    for (let num=0; num<10; num++) {
      if (isUsed[num]) continue;
      isUsed[num] = true;
      charConvert.set(charKeys[idx], num);
      dfs(idx + 1);
      isUsed[num] = false;
    }
  }
};

// 그리디(가중치 정렬)
const solution2 = (input) => {
  const words = input.slice(1,).map(v => v.trim());
  const sumValue = new Map();

  for (const word of words) {
    for (let i=0; i<word.length; i++) {
      const char = word[i];
      if (!sumValue.get(char)) sumValue.set(char, 0);
      sumValue.set(char, sumValue.get(char) + Math.pow(10, word.length - i - 1));
    }
  }

  const chars = Array.from(sumValue.keys());
  chars.sort((a, b) => sumValue.get(b) - sumValue.get(a));

  let answer = 0;
  let num = 9;
  for (const char of chars) {
    answer += sumValue.get(char) * num--;
  }

  return answer;
}

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution2(input));
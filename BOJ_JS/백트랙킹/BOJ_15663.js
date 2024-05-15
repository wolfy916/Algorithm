/**
 * 제목 : N과 M (9)
 * 난이도 : 실버 2
 * 분류 : 백트랙킹
 */

/**
 * 접근 방식
 * 1. 백트랙킹을 적용한 dfs로 순열을 생성
 * 2. set 자료형을 사용하여 중복 제거
 */

const solution = (input) => {
  const [N, M] = input[0].split(" ").map(v => +v);
  const nums = input[1].split(" ").map(v => +v).sort((a, b) => a - b);

  const answer = new Set();
  const used = Array.from({ length: N }, () => false);
  genPerm([]);

  return Array.from(answer).join('\n');

  function genPerm(selected) {
    const len = selected.length;
    if (len >= M) {
      const selectedString = selected.join(" ");
      if (!answer.has(selectedString)) answer.add(selectedString);
      return;
    }

    for (let i=0; i<N; i++) {
      if (used[i]) continue;
      used[i] = true;
      selected.push(nums[i]);
      genPerm(selected);
      used[i] = false;
      selected.pop();
    }
  } 
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
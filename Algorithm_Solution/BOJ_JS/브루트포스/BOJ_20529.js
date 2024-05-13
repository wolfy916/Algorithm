/**
 * 제목 : 가장 가까운 세 사람의 심리적 거리 - 백준 실버 1
 * 분류 : 브루트 포스
 */

/**
 * 접근 방식
 * 1. N이 32보다 크면 무조건 최소거리 0
 * 2. 완전 탐색
 */

const solution = (input) => {
  const elements = [
    ["E", "I"],
    ["S", "N"],
    ["T", "F"],
    ["J", "P"],
  ];
  const mbtiArr = genMBTi([""], 0);

  let line = 0;
  const T = +input[line++];
  const answer = [];
  for (let i = 0; i < T; i++) {
    const N = +input[line++];
    if (N > 32) {
      answer.push(0);
      line++;
      continue;
    }

    const mbtiCntObj = {};
    for (const mbti of mbtiArr) {
      mbtiCntObj[mbti] = 0;
    }

    let students = input[line++].trim().split(" ");
    let flag = false;
    for (const student of students) {
      if (mbtiCntObj[student] > 1) {
        flag = true;
        break;
      }
      mbtiCntObj[student]++;
    }

    if (flag) {
      answer.push(0);
      continue;
    }

    students = [];
    for (const mbti of mbtiArr) {
      while (mbtiCntObj[mbti]-- > 0) students.push(mbti);
    }

    let result = 12;
    const len = students.length;
    for (let a = 0; a < len - 2; a++) {
      for (let b = a + 1; b < len - 1; b++) {
        for (let c = b + 1; c < len; c++) {
          result = Math.min(
            result,
            distance(students[a], students[b]) +
              distance(students[b], students[c]) +
              distance(students[c], students[a])
          );
        }
      }
    }

    answer.push(result);
  }

  return answer.join("\n");

  function genMBTi(arr, idx) {
    if (idx > 3) return arr;
    const result = [];
    for (let mbti of arr) {
      for (let i = 0; i < 2; i++) {
        result.push(mbti + elements[idx][i]);
      }
    }
    return genMBTi(result, idx + 1);
  }

  function distance(a, b) {
    let cnt = 0;
    for (let i = 0; i < 4; i++) {
      if (a[i] != b[i]) cnt++;
    }
    return cnt;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
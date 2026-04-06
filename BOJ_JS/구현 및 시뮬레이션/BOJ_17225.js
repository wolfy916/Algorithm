/**
 * 제목 : 세훈이의 선물가게
 * 난이도 : 골드 5
 * 분류 : 구현 및 시뮬레이션, 정렬
 */

const solution = (input) => {
  const [A, B, N] = input[0].split(" ").map(Number);

  let bTime = 0; // 상민
  let rTime = 0; // 지수

  const events = [];

  let line = 1;
  for (let i = 0; i < N; i++) {
    const [tStr, c, mStr] = input[line++].split(" ");
    const t = Number(tStr);
    const m = Number(mStr);

    if (c === "B") {
      if (bTime < t) bTime = t;

      for (let j = 0; j < m; j++) {
        events.push([bTime, "B"]);
        bTime += A;
      }
    } else {
      if (rTime < t) rTime = t;

      for (let j = 0; j < m; j++) {
        events.push([rTime, "R"]);
        rTime += B;
      }
    }
  }

  // 정렬: 시간 → B 우선
  events.sort((a, b) => {
    if (a[0] === b[0]) {
      if (a[1] === b[1]) return 0;
      return a[1] === "B" ? -1 : 1;
    }
    return a[0] - b[0];
  });

  const bResult = [];
  const rResult = [];

  let giftNumber = 1;

  for (const [, color] of events) {
    if (color === "B") {
      bResult.push(giftNumber);
    } else {
      rResult.push(giftNumber);
    }
    giftNumber++;
  }

  let answer = "";
  answer += bResult.length + "\n";
  answer += bResult.join(" ") + "\n";
  answer += rResult.length + "\n";
  answer += rResult.join(" ");

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
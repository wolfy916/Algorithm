/**
 * 제목 : 세훈이의 선물가게
 * 난이도 : 골드 5
 * 분류 : 구현 및 시뮬레이션, 정렬
 */

const solution = (input) => {
  const [A, B, _] = input[0].split(" ").map(Number);
  const orders = input.slice(1).map((line) => {
    const [t, c, m] = line.split(" ");
    return [Number(t), c, Number(m)];
  });

  const needTime = { B: A, R: B };

  const tasks = [];
  for (const [time, color, count] of orders) {
    for (let i = 0; i < count; i++) {
      tasks.push({ time, color });
    }
  }

  tasks.sort((a, b) => {
    if (a.time === b.time) {
      return a.color === "B" ? -1 : 1;
    }
    return a.time - b.time;
  });

  const nextAvailable = { B: 0, R: 0 };
  const result = [];

  for (const { time, color } of tasks) {
    const start = Math.max(time, nextAvailable[color]);
    const end = start + needTime[color];

    result.push({ end, color });

    nextAvailable[color] = end;
  }

  result.sort((a, b) => {
    if (a.end === b.end) {
      return a.color === "B" ? -1 : 1;
    }
    return a.end - b.end;
  });

  const log = { B: [], R: [] };
  let number = 1;

  for (const item of result) {
    log[item.color].push(number++);
  }

  const answer = `${log.B.length}\n${log.B.join(" ")}\n${log.R.length}\n${log.R.join(" ")}`;

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
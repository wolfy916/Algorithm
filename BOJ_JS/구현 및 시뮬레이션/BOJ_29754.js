/**
 * 제목 : 세상에는 많은 유튜버가 있고, 그중에서 버츄얼 유튜버도 존재한다
 * 난이도 : 실버 1
 * 분류 : 구현
 */

const solution = (input) => {
  const [N, M] = input[0].split(" ").map(Number);
  const week = M / 7;
  const log = new Map();

  let name, day, startTime, endTime, w, arr;
  for (let i = 1; i < N + 1; i++) {
    [name, day, startTime, endTime] = input[i].split(" ");

    day = Number(day);
    startTime = startTime.split(':').map(Number);
    endTime = endTime.split(':').map(Number);
    time = endTime[0] * 60 + endTime[1] - startTime[0] * 60 - startTime[1];
    w = Math.floor((day - 1) / 7);

    if (log.has(name)) {
      arr = log.get(name);
    } else {
      arr = Array.from(Array(week), () => Array(2).fill(0));
    }

    arr[w][0] += 1;
    arr[w][1] += time;
    log.set(name, arr);
  }

  const answer = [];
  log.forEach((tb, nm) => {
    let real = true;
    for (let i = 0; i < week; i++) {
      if (tb[i][1] < 3600 || tb[i][0] < 5) {
        real = false;
        break;
      }
    }
    if (real) answer.push(nm);
  });

  return answer.length > 0 ? answer.sort().join("\n") : -1;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
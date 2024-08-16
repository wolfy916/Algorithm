/**
 * 제목 : 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1
 * 난이도 : 골드 3
 * 분류 : 누적합
 */

const solution = (input) => {
  const N = Number(input[0]);
  const schedule = new Map();

  for (let i=1; i<N + 1; i++) {
    const [t_x, t_e] = input[i].split(" ").map(Number);

    if (schedule.get(t_x)) {
      schedule.set(t_x, schedule.get(t_x) + 1);
    } else {
      schedule.set(t_x, 1);
    }

    if (schedule.get(t_e)) {
      schedule.set(t_e, schedule.get(t_e) - 1);
    } else {
      schedule.set(t_e, -1);
    }
  }
  
  const keys = Array.from(schedule.keys());
  keys.sort((a, b) => a - b);

  for (let i=0; i<keys.length - 1; i++) {
    schedule.set(keys[i + 1], schedule.get(keys[i + 1]) + schedule.get(keys[i]));
  }

  let [a_x, a_e] = [0, 0];
  let answer = 0;
  let isSearching = false;
  
  for (const key of keys) {
    if (answer < schedule.get(key)) {
      a_x = key;
      answer = schedule.get(key);
      isSearching = true;
    }

    if (isSearching && schedule.get(key) < answer) {
      a_e = key;
      isSearching = false;
    }
  }
  
  return answer + '\n' + a_x + " " + a_e;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
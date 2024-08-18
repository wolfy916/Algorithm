/**
 * 제목 : 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1
 * 난이도 : 골드 3
 * 분류 : 누적합, 정렬, 값과 좌표 압축
 */

const solution = (input) => {
  const N = Number(input[0]);
  const startArr = Array.from(Array(N), () => 0);
  const endArr = Array.from(Array(N), () => 0);
  const temp = new Set();

  for (let i = 0; i < N; i++) {
    const [t_x, t_e] = input[i + 1].split(" ").map(Number);
    startArr[i] = t_x;
    endArr[i] = t_e;
    temp.add(t_x);
    temp.add(t_e);
  }

  const idx = Array.from(temp);
  idx.sort((a, b) => a - b);

  const sumArr = Array.from(Array(idx.length), () => 0);
  for (let i = 0; i < N; i++) {
    const startTime = binSearch(startArr[i]);
    const endTime = binSearch(endArr[i]);
    sumArr[startTime]++;
    sumArr[endTime]--;
  }

  for (let i = 1; i < sumArr.length; i++) {
    sumArr[i] += sumArr[i - 1];
  }

  let answer = 0;
  let maxStartIdx = -1;
  let maxEndIdx = -1;
  for (let i = 0; i < idx.length; i++) {
    if (answer < sumArr[i]) {
      maxStartIdx = i;
      maxEndIdx = i;
      answer = sumArr[i];
    }

    if (sumArr[i] === answer && i - 1 === maxEndIdx) {
      maxEndIdx = i;
    }
  }

  return answer + "\n" + idx[maxStartIdx] + " " + idx[maxEndIdx + 1];

  function binSearch(value) {
    let [left, right] = [0, idx.length - 1];
    let mid;
    while (left <= right) {
      mid = Math.floor((left + right) / 2);
      if (idx[mid] < value) {
        left = mid + 1;
      } else if (idx[mid] > value) {
        right = mid - 1;
      } else break;
    }
    return mid;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 랜선 자르기
 * 난이도 : 실버 2
 * 분류 : 이분 탐색
 */

const solution = (input) => {
  let [line, ...arr] = input;
  const [K, N] = line.split(" ").map(v => +v);
  arr = arr.map(v => +v);

  let [left, right] = [0, Math.pow(2, 31)];
  let answer = 0;
  let mid;
  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    if (check(mid)) {
      answer = Math.max(answer, mid);
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return answer;

  function check(mid) {
    let cnt = 0;
    for (let i=0; i<K; i++) {
      cnt += Math.floor(arr[i] / mid);
    }
    if (cnt >= N) return true;
    else return false;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
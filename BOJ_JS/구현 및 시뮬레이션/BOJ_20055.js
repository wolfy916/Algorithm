/**
 * 제목 : 컨베이어 벨트 위의 로봇
 * 난이도 : 골드 5
 * 분류 : 구현 및 시뮬레이션
 */

const solution = (input) => {
  const [N, K] = input[0].split(" ").map(Number);
  const A = input[1].split(" ").map(Number).reverse();
  const robots = Array.from(Array(2 * N), () => 0);
  let [s, e] = [2 * N - 1, N];
  let zeroCount = 0;
  let answer = 0;

  while (zeroCount < K) {
    // 단계 카운트
    answer++;

    // 1번 과정
    s = (s + 1) % (2 * N);
    e = (e + 1) % (2 * N);
    robots[e] = 0;

    // 2번 과정
    if (s < e) {
      for (let i=e + 1; i < 2 * N; i++) {
        process2(i);
      }
      for (let i=0; i < s + 1; i++) {
        process2(i);
      }
    } else {
      for (let i=e + 1; i < s + 1; i++) {
        process2(i);
      }
    }
    robots[e] = 0;
    
    // 3번 과정
    if (A[s] > 0) {
      robots[s] = 1;
      if (--A[s] === 0) zeroCount++;
    }

  }

  return answer;

  function process2(idx) {
    if (robots[idx] === 0) return;
    const nxt = getNxtIdx(idx);
    if (robots[nxt] === 1 || A[nxt] === 0) return;
    robots[idx] = 0;
    robots[nxt] = 1;
    if (--A[nxt] === 0) zeroCount++;
  }

  function getNxtIdx(i) {
    return 0 < i ? i - 1 : 2 * N - 1;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
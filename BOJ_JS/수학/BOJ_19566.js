/**
 * 제목 : 수열의 구간 평균
 * 난이도 : 골드 2
 * 분류 : 수학(평균), 누적합
 */

// 개인적으로 너무 어려운 문제..

const solution = (input) => {
  // 입력 및 데이터 초기화
  const [N, K] = input[0].split(" ").map(Number);
  const A = input[1].split(" ").map((v) => BigInt(v));

  // 누적합 리스트 생성
  A.unshift(0n);
  for (let i = 2; i < N + 1; i++) A[i] += A[i - 1];

  // d[i] = (0 ~ i까지의 누적합) - (주어진 평균값 K) * (구간 길이 i);
  // d[i]와 d[j]의 값이 같다면, i ~ j 구간의 평균이 K인 원리
  const d = Array(N + 1);
  for (let i = 0; i < N + 1; i++) d[i] = A[i] - BigInt(K) * BigInt(i);

  // d 배열의 원소값별로 카운팅
  const count = {};
  for (let i = 0; i < N + 1; i++) {
    if (count[d[i]]) {
      count[d[i]] += 1;
    } else {
      count[d[i]] = 1;
    }
  }

  // d값이 같은 구간들 중에서 2개의 구간을 고르는 조합의 수들을 모두 더함
  let answer = 0;
  for (const c of Object.values(count)) {
    answer += Math.floor((c * (c - 1)) / 2);
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
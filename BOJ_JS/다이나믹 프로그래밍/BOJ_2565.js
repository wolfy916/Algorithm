/**
 * 제목 : 전깃줄
 * 난이도 : 골드 5
 * 분류 : 다이나믹 프로그래밍
 */

const solution = (input) => {
  const N = Number(input[0]);
  const infos = input.slice(1,).map(v => v.split(" ").map(Number));
  
  infos.sort((a, b) => a[0] - b[0]);

  // dp[i] = i번째 전깃줄을 선택하였을때 교차되지 않는 전깃줄 최대 개수
  const dp = Array.from({ length: N + 1 }, () => 1);

  for (let i=1; i<N; i++) {
    // j(= 0 ~ i-1)번 전깃줄 중
    for (let j=0; j<i; j++) {
      // i번째 전깃줄과 교차되지 않는다면
      if (infos[i][1] > infos[j][1]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return N - Math.max(...dp);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
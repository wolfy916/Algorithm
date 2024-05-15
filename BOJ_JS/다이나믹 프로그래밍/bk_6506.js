// 엘 도라도

const solution = (input) => {
  let line = 0
  while (true) {
    const [n, k] = input[line++].split(" ").map((v) => +v);
    if (n === 0 && k === 0) break;
    const arr = input[line++].split(" ").map((v) => +v);
    const dp = Array.from({ length: n }, () => 
      Array.from({ length: k + 1 }, () => 0)
    );
    let count = 0;
    for (let i = 0; i < n; i++) {
      dp[i][1] = 1;
      for (let j = 0; j < i; j++) {
        if (arr[j] >= arr[i]) continue;
        let tmp = Math.min(i + 1, k);
        for (let c = 1; c < tmp; c++) {
          dp[i][c + 1] += dp[j][c];
        }
      }
      count += dp[i][k];
    }
    console.log(count);
  }
};

// 데이터 입력 및 메인 함수 실행
const input = require("fs").readFileSync("./input.txt").toString().split("\n");
solution(input);
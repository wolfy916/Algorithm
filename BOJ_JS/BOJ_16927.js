/**
 * 제목 : 배열 돌리기 2
 * 난이도 : 골드 5
 * 분류 : 
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M, R] = convert(input.shift());
  const midN = Math.floor(N / 2);
  const midM = Math.floor(M / 2);

  console.log(midN, midM);

  const answer = Array.from(Array(N), () => Array(M));

  for (let i=0; i<N; i++) {
    input[i] = convert(input[i]);
  }

  for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
      let line = 0;
      let n = N;
      let m = M;
      while (n === N) {
        
      }
      answer[i][j] = 
    }
  }
  
  return answer.map(v => v.join(" ")).join("\n");

  function changeRotatedState(i, j) {
    
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
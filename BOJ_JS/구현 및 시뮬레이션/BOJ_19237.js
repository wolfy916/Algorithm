/**
 * 제목 : 어른 상어
 * 난이도 : 골드 1
 * 분류 : 구현 및 시뮬레이션
 */

class Shark {
  constructor() {
    this.i = null;
    this.j = null;
    this.direction = null;
    this.priority = Array.from(Array(4), () => Array(4));
    this.isRunAway = false;
  }
}

const solution = (input) => {
  const convert = s => s.split(" ").map(Number);
  const [N, M, K] = convert(input[0]);
  const sharkArea = Array.from(Array(N), () => Array(N));
  const sharks = Array.from(Array(M + 1), () => new Shark());
  const smellArea = Array.from(Array(N), () => {
    return Array.from(Array(N), () => [0, 0]);
  });
  const direction = convert(input[N + 1]);
  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];
  let sharkCount = M;
  let answer = 1;
  
  for (let i=1; i<N + 1; i++) {
    const line = convert(input[i]);
    for (let j=0; j<N; j++) {
      if (line[j] > 0) {
        sharks[line[j]].i = i - 1;
        sharks[line[j]].j = j;
      }
      sharkArea[i - 1][j] = line[j];
    }
  }

  for (let i=1; i<M + 1; i++) {
    sharks[i].direction = direction[i - 1] - 1;
  }

  let p = 0;
  for (let i=N + 2; i<N + 2 + M * 4; i++) {
    const line = convert(input[i]);
    const sharkIdx = Math.floor((i - N - 2) / 4) + 1;
    for (let j=0; j<4; j++) {
      sharks[sharkIdx].priority[p][j] = line[j] - 1;
    }
    p = (p + 1) % 4;
  }

  spraySmell();
  
  while (answer <= 1000) {
    
    // 상어이동
    sharkMove();
    
    // 냄새 줄이기
    decreaseSmell();
    
    // 냄새 남기기
    spraySmell();

    if (sharkCount === 1) break;

    answer++;
  }

  return answer > 1000 ? -1 : answer;

  function spraySmell() {
    for (let k=1; k<M + 1; k++) {
      if (sharks[k].isRunAway) continue;
      smellArea[sharks[k].i][sharks[k].j][0] = k;
      smellArea[sharks[k].i][sharks[k].j][1] = K;
    }
  }

  function isValid(i, j) {
    return i < 0 || j < 0 || i >= N || j >= N ? false : true;
  }

  function isExistedBlank(i, j) {
    let result = false;
    for (let k=0; k<4; k++) {
      const ni = i + di[k];
      const nj = j + dj[k];
      if (!isValid(ni, nj)) continue;
      if (smellArea[ni][nj][1] > 0) continue;
      result = true;
      break;
    }
    return result;
  }

  function sharkMove() {
    const move = Array.from(Array(M + 1), () => [0, 0]);

    for (let i=1; i<M + 1; i++) {
      if (sharks[i].isRunAway) continue;
      const d = sharks[i].direction;
      const flag = isExistedBlank(sharks[i].i, sharks[i].j);
      for (let k=0; k<4; k++) {
        const ni = sharks[i].i + di[sharks[i].priority[d][k]];
        const nj = sharks[i].j + dj[sharks[i].priority[d][k]];
        if (!isValid(ni, nj)) continue;
        if (smellArea[ni][nj][1] > 0 && (smellArea[ni][nj][0] !== i || flag)) continue;
        sharkArea[sharks[i].i][sharks[i].j] = 0;
        move[i][0] = ni;
        move[i][1] = nj;
        sharks[i].direction = sharks[i].priority[d][k];
        break;
      }
    }

    for (let i=M; i>0; i--) {
      if (sharks[i].isRunAway) continue;
      const ni = move[i][0];
      const nj = move[i][1];
      if (sharkArea[ni][nj] > 0) {
        sharks[sharkArea[ni][nj]].isRunAway = true;
        sharkCount -= 1;
      }
      sharkArea[ni][nj] = i;
      sharks[i].i = ni;
      sharks[i].j = nj;
    }
  }

  function decreaseSmell() {
    for (let i=0; i<N; i++) {
      for (let j=0; j<N; j++) {
        if (smellArea[i][j][1] > 0) {
          smellArea[i][j][1]--;
        }
        
        if (smellArea[i][j][1] === 0) {
          smellArea[i][j][0] = 0;
        }
      }
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
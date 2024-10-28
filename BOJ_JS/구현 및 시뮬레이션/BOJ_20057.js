/**
 * 제목 : 마법사 상어와 토네이도
 * 난이도 : 골드 3
 * 분류 : 구현 및 시뮬레이션
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const N = Number(input[0]);
  const area = input.slice(1,).map(convert);
  const initTotalV = area.reduce((a, c) => a + c.reduce((aa, cc) => aa + cc), 0);
  const di = [0, 1, 0, -1];
  const dj = [-1, 0, 1, 0];
  const coords1 = [
    [[-1, 1], [1, 1]],
    [[-1, -1], [-1, 1]],
    [[-1, -1], [1, -1]],
    [[1, -1], [1, 1]]
  ];
  const coords2 = [
    [[-2, 0], [2, 0]],
    [[0, -2], [0, 2]],
    [[-2, 0], [2, 0]],
    [[0, -2], [0, 2]]
  ];
  const coords5 = [[0, -2], [2, 0], [0, 2], [-2, 0]];
  const coords7 = [
    [[-1, 0], [1, 0]],
    [[0, -1], [0, 1]],
    [[-1, 0], [1, 0]],
    [[0, -1], [0, 1]]
  ];
  const coords10 = [
    [[-1, -1], [1, -1]],
    [[1, -1], [1, 1]],
    [[-1, 1], [1, 1]],
    [[-1, -1], [-1, 1]]
  ];

  let [vi, vj] = [Math.floor(N / 2), Math.floor(N / 2)];
  let count = 1;
  let k = 0;
  while (vi !== 0 || vj !== 0) {
    for (let i=0; i<Math.ceil(count / 2); i++) {
      vi += di[k];
      vj += dj[k];
      sandBlow(vi, vj, k);
      if (vi === 0 && vj === 0) break;
    }
    k = (k + 1) % 4;
    count++;
  }
  
  const curTotalV = area.reduce((a, c) => a + c.reduce((aa, cc) => aa + cc), 0);
  const answer = initTotalV - curTotalV;

  return answer;

  function isValid(i, j) {
    if (i < 0 || j < 0 || i >= N || j >= N) return false;
    return true;
  }

  function moveSand(vi, vj, coords, multiple, k, amount) {
    let ni, nj, v;
    for (const [di, dj] of coords[k]) {
      ni = vi + di;
      nj = vj + dj;
      v = Math.floor(area[vi][vj] * multiple);
      amount -= v;
      if (!isValid(ni, nj)) continue;
      area[ni][nj] += v;
    }
    return amount;
  }

  function sandBlow(vi, vj, k) {
    let amount = area[vi][vj];
    let ni, nj, v;

    amount = moveSand(vi, vj, coords1, 0.01, k, amount);
    amount = moveSand(vi, vj, coords2, 0.02, k, amount);
    amount = moveSand(vi, vj, coords7, 0.07, k, amount);
    amount = moveSand(vi, vj, coords10, 0.1, k, amount);

    ni = vi + coords5[k][0];
    nj = vj + coords5[k][1];
    v = Math.floor(area[vi][vj] * 0.05);
    amount -= v;
    if (isValid(ni, nj)) {
      area[ni][nj] += v;
    }

    ni = vi + di[k];
    nj = vj + dj[k];
    if (isValid(ni, nj)) {
      area[ni][nj] += amount;
    }

    area[vi][vj] = 0;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
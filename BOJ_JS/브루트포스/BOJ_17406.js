/**
 * 제목 : 배열 돌리기 4
 * 난이도 : 골드 4
 * 분류 : 브루트 포스, 구현, 백트랙킹
 */

const convToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, M, K] = convToNumArr(input[0]);
  const [arr, cal] = [
    input.slice(1, N + 1).map(v => convToNumArr(v)),
    input.slice(N + 1,).map(v => convToNumArr(v)),
  ];

  const delta = [
    [[0, 1], [1, 0], [0, -1], [-1, 0]],
    [[1, 0], [0, 1], [-1, 0], [0, -1]],
  ];
  const rotate = (r, c, s, arr, d) => {
    if (s === 0) return arr;
    let [si, sj] = [r - s - 1, c - s - 1];
    let deltaIdx = 0;
    let [di, dj] = delta[d][deltaIdx];
    let [vi, vj] = [si + di, sj + dj];
    let temp = arr[si][sj];
    while (vi !== si || vj !== sj) {
      [arr[vi][vj], temp] = [temp, arr[vi][vj]];
      [di, dj] = delta[d][deltaIdx];
      let [ni, nj] = [vi + di, vj + dj];
      if (ni < r - s - 1 || nj < c - s - 1 || ni >= r + s || nj >= c + s) {
        [di, dj] = delta[d][++deltaIdx];
        [ni, nj] = [vi + di, vj + dj];
      }
      [vi, vj] = [ni, nj];
    }
    [arr[vi][vj], temp] = [temp, arr[vi][vj]];
    return rotate(r, c, s - 1, arr, d);
  }

  let answer = Infinity;
  const isUsed = Array.from({ length: K }, () => false);
  const permutation = (arr, cnt) => {
    if (cnt >= K) {
      answer = Math.min(answer, arr.reduce((acc, cur) => Math.min(acc, cur.reduce((acc, cur) => acc + cur)), Infinity))
      return;
    }
    for (let i=0; i<K; i++) {
      if (isUsed[i]) continue;
      isUsed[i] = true;
      rotate(...cal[i], arr, 0);
      permutation(arr, cnt + 1);
      isUsed[i] = false;
      rotate(...cal[i], arr, 1);
    }
  }

  permutation(arr, 0);

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
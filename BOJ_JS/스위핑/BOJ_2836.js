/**
 * 제목 : 수상 택시
 * 난이도 : 골드 3
 * 분류 : 스위핑, 정렬, 그리디?
 */

const solution = (input) => {
  const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

  const [[N, M], info] = [convertToNumArr(input[0]), input.slice(1,).map(v => convertToNumArr(v).reverse()).filter((v) => v[0] < v[1])];

  if (N < 1) return M;

  info.sort((a, b) => a[0] - b[0]);

  const selected = [];
  let [s, e] = info[0];
  for (const [left, right] of info.slice(1,)) {
    if (left <= e && e < right) {
      e = right;
    } else if (e < left) {
      selected.push([s, e]);
      [s, e] = [left, right];
    }
  }
  selected.push([s, e]);

  return M + selected.reduce((acc, cur) => acc + (cur[1] - cur[0]) * 2, 0);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
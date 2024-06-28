/**
 * 제목 : 로봇 프로젝트
 * 난이도 : 골드 5
 * 분류 : 투 포인터
 */

const solution = (x, N, legos) => {
  if (N < 2) return "danger"; // 0개 혹은 1개라면 2개를 고를 수 없음.

  // [1] 레고들을 오름차순으로 정렬
  legos.sort((a, b) => a - b);

  // [2] 투 포인터 풀이
  let [p1, p2] = [0, N - 1];
  while (p1 < p2) {
    const sumV = legos[p1] + legos[p2];
    // x보다 크면 p2를 왼쪽으로 이동
    if (x < sumV) {
      p2--;
      // x보다 작으면 p1을 오른쪽으로 이동
    } else if (sumV < x) {
      p1++;
      // 찾으면 바로 return
    } else return `yes ${legos[p1]} ${legos[p2]}`;
  }

  return "danger";
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let index = 0;
let x = null;
let N = null;
let legos = [];

rl.on("line", (line) => {
  if (index === 0) x = Number(line) * 1e7;
  else if (index === 1) {
    N = Number(line);
    if (N === 0) {
      console.log('danger');
      index = -1;
    };
  } else if (index === N + 1) {
    legos.push(Number(line));
    console.log(solution(x, N, legos));
    legos = [];
    index = -1;
  } else {
    legos.push(Number(line));
  }
  index++;
}).on("close", () => {
  process.exit();
});
/**
 * 제목 : 트리와 쿼리
 * 난이도 : 골드5
 * 분류 : 트리
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, R, Q] = convert(input[0]);

  const adjL = Array.from(Array(N + 1), () => []);
  let u, v;
  for (let i = 1; i < N; i++) {
    [u, v] = convert(input[i]);
    adjL[u].push(v);
    adjL[v].push(u);
  }

  const count = Array(N + 1).fill(0);
  countChild(R);

  const answer = [];
  for (let i = N; i < N + Q; i++) {
    answer.push(count[Number(input[i])]);
  }

  return answer.join("\n");

  function countChild(v) {
    count[v]++;
    for (const w of adjL[v]) {
      if (count[w] > 0) continue;
      count[v] += countChild(w);
    }
    return count[v];
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
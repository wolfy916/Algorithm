/**
 * 제목 : ABCDE
 * 난이도 : 골드5
 * 분류 : 백트랙킹
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, M] = convert(input[0]);
  const adjL = Array.from({ length: N }, () => []);
  const visited = Array(N);

  for (let i=1; i<M + 1; i++) {
    const [a, b] = convert(input[i]);
    adjL[a].push(b);
    adjL[b].push(a);
  }

  const nums = Array.from({ length: N }, (_, i) => i);
  nums.sort((a, b) => adjL[a].length - adjL[b].length);

  for (const num of nums) {
    if (visited[num]) continue;
    visited[num] = true;
    if (dfs(1, num)) return 1;
  }

  return 0;

  function dfs(cnt, v) {
    if (cnt >= 5) return true;

    for (const w of adjL[v]) {
      if (visited[w]) continue;
      visited[w] = true;
      if (dfs(cnt + 1, w)) return true;
      visited[w] = false;
    }

    return false;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
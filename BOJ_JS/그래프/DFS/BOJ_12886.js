/**
 * 제목 : 돌 그룹
 * 난이도 : 골드 4
 * 분류 : DFS(스택)
 */

const solution = (input) => {
  const nums = input.split(" ").map(Number);
  const sum = nums.reduce((a, c) => a + c, 0);
  if (sum % 3) return 0;
  return dfs(sum, nums);

  function dfs(sum, nums) {
    const visited = Array.from({ length: 1500 }, () => {
      return Array.from({ length: 1500 }, () => 0);
    });
    visited[nums[0]][nums[1]] = 1;
    const stack = [nums];
    
    while (stack.length) {
      const v = stack.pop();
      for (let i=0; i<3; i++) {
        for (let j=0; j<3; j++) {
          if (v[i] < v[j]) {
            const w = [v[i] * 2, v[j] - v[i], sum - v[i] - v[j]];
            if (visited[w[0]][w[1]]) continue;
            visited[w[0]][w[1]] = 1;
            stack.push(w);
          }
        }
      }
    }

    return visited[sum / 3][sum / 3];
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();
console.log(solution(input));
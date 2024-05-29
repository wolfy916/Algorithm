/**
 * 제목 : 게임 개발
 * 난이도 : 골드 3
 * 분류 : 위상 정렬
 */

const solution = (input) => {
  const [N, buildings] = [
    +input[0],
    input.slice(1,).map(v => v.split(" ").map(Number)),
  ];

  const answer = Array.from({ length: N }, () => 0);

  const memoizate = (num) => {
    const [time, ...nums] = buildings[num - 1];
    let maxV = 0;
    for (let i=0; i<nums.length - 1; i++) {
      if (answer[nums[i] - 1] < 1) memoizate(nums[i]);
      maxV = Math.max(maxV, answer[nums[i] - 1]);
    }
    answer[num - 1] = time + maxV;
  }

  for (let i=0; i<N; i++) {
    if (answer[i] > 0) continue;
    memoizate(i + 1);
  }

  return answer.join('\n');
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
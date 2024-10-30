/**
 * 제목 : 순열의 순서
 * 난이도 : 골드 5
 * 분류 : 구현
 */

const solution = (input) => {
  const N = Number(input[0]);
  const arr = input[1].split(" ").map((v) => BigInt(v));
  const isUsed = Array(N + 1).fill(false);
  const fa = Array.from(Array(N + 1), (_, i) => BigInt(i));

  fa[0] = 1n;
  for (let i = 1; i < N + 1; i++) fa[i] *= fa[i - 1];

  let answer;
  if (arr[0] === 1n) {
    answer = Array(N + 1).fill(0);
    let k = arr[1];
    for (let i = 1; i < N + 1; i++) {
      let cnt = 1n;
      for (let j = 1; j < N + 1; j++) {
        if (isUsed[j]) continue;
        if (k <= cnt * fa[N - i]) {
          k -= (cnt - 1n) * fa[N - i];
          answer[i] = j;
          isUsed[j] = true;
          break;
        }
        cnt += 1n;
      }
    }

    answer.shift();
    answer = answer.join(" ");
  } else {
    let k = 1n;
    for (let i = 1; i < N + 1; i++) {
      let cnt = 0n;
      for (let j = 1; j < arr[i]; j++) {
        if (isUsed[j]) continue;
        cnt += 1n;
      }
      k += cnt * fa[N - i];
      isUsed[arr[i]] = true;
    }
    answer = k.toString();
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
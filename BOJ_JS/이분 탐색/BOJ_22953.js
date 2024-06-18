/**
 * 제목 : 도도의 음식 준비
 * 난이도 : 골드 4
 * 분류 : 이분 탐색, 백트랙킹
 */

/**
 * 접근 방식
 * 1. 격려 조합을 적용
 * 2. 이분탐색으로 최소시간 갱신
 */

const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, K, C] = convertToNumArr(input[0]);
  const A = convertToNumArr(input[1]);

  let answer = Infinity;

  dfs(0, 0);

  return answer;

  function dfs(idx, cnt) {
    if (cnt >= C) {
      answer = Math.min(answer, binSeach());
      return;
    }
    let flag = true;
    for (let i=idx; i<N; i++) {
      if (A[i] < 2) continue;
      flag = false;
      A[i]--;
      dfs(i, cnt + 1);
      A[i]++;
    }
    if (flag) answer = Math.min(answer, binSeach());
  }

  function binSeach() {
    let [left, right] =  [0, 1e12];
    let mid, result;
    while (left <= right) {
      mid = Math.floor((left + right) / 2);
      if (check(mid)) {
        right = mid - 1;
        result = mid;
      } else {
        left = mid + 1;
      }
    }
    return result;
  }

  function check(time) {
    let cnt = 0;
    for (let i=0; i<N; i++) {
      cnt += Math.floor(time / A[i]);
    }
    return cnt >= K ? true : false;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
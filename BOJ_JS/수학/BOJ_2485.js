/**
 * 제목 : 가로수
 * 난이도 : 실버 4
 * 분류 : 수학, 최대공약수(유클리드 호제법)
 */

const solution = (input) => {
  const [N, trees] = [+input[0], input.slice(1,).map(Number)];

  // 재귀 GCD
  const getGCD1 = (a, b) => b > 0 ? getGCD1(b, a % b) : a;

  // 반복문 GCD
  const getGCD2 = (a, b) => {
    while (b > 0) {
      [a, b] = [b, a % b];
    }
    return a;
  }

  // 최대공약수(GCD)를 이용한 최소공배수(LCM) 구하기
  const getLCM = (a, b) => {
    const GCD = getGCD1(a, b);
    return a * b / GCD;
  }

  for (let i=0; i<N - 1; i++) {
    trees[i] = trees[i + 1] - trees[i];
  }

  trees.pop();

  let gcd = trees[0];
  for (let i=1; i<N; i++) {
    gcd = getGCD2(gcd, trees[i]);
  }

  return trees.reduce((acc, cur) => acc + cur / gcd - 1, 0);
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
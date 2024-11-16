/**
 * 제목 : 양 한 마리... 양 A마리... 양 A제곱마리...
 * 난이도 : 골드 3
 * 분류 : 수학, 분할정복
 */

// 등비수열의 합 S = a_0 * (r^(n + 1) - 1) / (r - 1)

const solution = (input) => {
  const [A, B] = input[0].split(" ").map((v, i) => i === 0 ? Number(v) : BigInt(v));
  const MOD = 1e9 + 7;
  const memoization = Array(B / 2n + 1n).fill(0);

  memoization[0] = 1;
  memoization[1] = A;

  const answer = (getExponentiation(B) - 1) / (A - 1);

  return answer;

  function getExponentiation(n) {
    if (memoization[n]) return memoization[n];

    const half = n / 2n;
    const a = getExponentiation(half);
    const b = getExponentiation(n % 2n ? half : half - 1n);
    const result = A * (a % MOD) * (b % MOD);

    if (n < memoization.length) memoization[n] = result % MOD;

    return result % MOD;
  }

};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
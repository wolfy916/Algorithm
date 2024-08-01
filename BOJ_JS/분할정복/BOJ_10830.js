/**
 * 제목 : 행렬 제곱
 * 난이도 : 골드 4
 * 분류 : 수학(행렬 거듭제곱), 분할정복
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, B] = input[0]
    .split(" ")
    .map((v, i) => (i < 1 ? Number(v) : BigInt(v)));
  const matrix = [];
  for (let i = 1; i < N + 1; i++) {
    matrix.push(convert(input[i]).map((v) => v % 1000));
  }

  return divideAndConquer(B)
    .map((v) => v.join(" "))
    .join("\n");

  function divideAndConquer(n) {
    if (n === BigInt(1)) return matrix;

    const dividedMatrix = divideAndConquer(n / BigInt(2));

    if (n % BigInt(2)) {
      return matrixSquare(matrixSquare(dividedMatrix, dividedMatrix), matrix);
    } else {
      return matrixSquare(dividedMatrix, dividedMatrix);
    }
  }

  function matrixSquare(a, b) {
    const resultMatrix = Array.from({ length: N }, () => {
      return Array.from({ length: N }, () => 0);
    });

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        for (let k = 0; k < N; k++) {
          resultMatrix[i][j] += a[i][k] * b[k][j];
          resultMatrix[i][j] %= 1000;
        }
      }
    }

    return resultMatrix;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
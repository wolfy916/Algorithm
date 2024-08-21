/**
 * 제목 : 배열 돌리기 3
 * 난이도 : 골드 5
 * 분류 : 구현
 */

const convert = (s) => s.split(" ").map(Number);

const solution = (input) => {
  const [N, M, _] = convert(input[0]);
  let A = Array.from(Array(N), (_, i) => convert(input[i + 1]));
  const R = convert(input[N + 1]);

  const functions = {
    1: (arr) => num1(arr),
    2: (arr) => num2(arr),
    3: (arr) => num3(arr),
    4: (arr) => num4(arr),
    5: (arr) => num5(arr),
    6: (arr) => num6(arr),
  };

  for (const r of R) {
    A = functions[r](A);
  }

  return A.map((v) => v.join(" ")).join("\n");

  function num1(arr) {
    const N = arr.length;
    const M = arr[0].length;
    const newArr = Array.from(Array(N), () => new Array(M));
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        newArr[N - i - 1][j] = arr[i][j];
      }
    }
    return newArr;
  }

  function num2(arr) {
    const N = arr.length;
    const M = arr[0].length;
    const newArr = Array.from(Array(N), () => new Array(M));
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        newArr[i][M - j - 1] = arr[i][j];
      }
    }
    return newArr;
  }

  function num3(arr) {
    const N = arr.length;
    const M = arr[0].length;
    const newArr = Array.from(Array(M), () => new Array(N));
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        newArr[j][N - i - 1] = arr[i][j];
      }
    }
    return newArr;
  }

  function num4(arr) {
    const N = arr.length;
    const M = arr[0].length;
    const newArr = Array.from(Array(M), () => new Array(N));
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        newArr[M - j - 1][i] = arr[i][j];
      }
    }
    return newArr;
  }

  function num5(arr) {
    const N = arr.length;
    const M = arr[0].length;
    const delta = [
      [0, 1],
      [1, 0],
      [-1, 0],
      [0, -1],
    ];
    const newArr = Array.from(Array(N), () => new Array(M));
    let k = 0;
    for (let di = 0; di < 2; di++) {
      for (let dj = 0; dj < 2; dj++) {
        for (let i = (di * N) / 2; i < ((di + 1) * N) / 2; i++) {
          for (let j = (dj * M) / 2; j < ((dj + 1) * M) / 2; j++) {
            newArr[i + (N / 2) * delta[k][0]][j + (M / 2) * delta[k][1]] =
              arr[i][j];
          }
        }
        k++;
      }
    }
    return newArr;
  }

  function num6(arr) {
    const N = arr.length;
    const M = arr[0].length;
    const delta = [
      [1, 0],
      [0, -1],
      [0, 1],
      [-1, 0],
    ];
    const newArr = Array.from(Array(N), () => new Array(M));
    let k = 0;
    for (let di = 0; di < 2; di++) {
      for (let dj = 0; dj < 2; dj++) {
        for (let i = (di * N) / 2; i < ((di + 1) * N) / 2; i++) {
          for (let j = (dj * M) / 2; j < ((dj + 1) * M) / 2; j++) {
            newArr[i + (N / 2) * delta[k][0]][j + (M / 2) * delta[k][1]] =
              arr[i][j];
          }
        }
        k++;
      }
    }
    return newArr;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
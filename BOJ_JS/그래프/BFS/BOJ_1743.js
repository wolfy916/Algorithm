/**
 * 제목 : 음식물 피하기
 * 난이도 : 실버 1
 * 분류 : bfs
 */

const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  // 데이터 입력
  const [N, M, _] = convertToNumArr(input[0]);
  const coords = input.slice(1,).map(convertToNumArr);
  
  // 2차원 배열 생성
  const area = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: M + 1 }, () => 0);
  });

  // 좌표 기록
  for (const [i, j] of coords) {
    area[i][j] = 1;
  }

  // 상하좌우 delta 값 설정
  const delta = [[-1, 0], [1, 0], [0, -1], [0, 1]];

  // bfs 함수
  const calculateFoodSize = (si, sj) => {
    let foodSize = 1;
    area[si][sj] = 0;
    const queue = [[si, sj]];
    while (queue.length > 0) {
      const [vi, vj] = queue.shift();
      for (const [di, dj] of delta) {
        const [ni, nj] = [vi + di, vj + dj];
        if (ni < 1 || nj < 1 || ni > N || nj > M) continue;
        if (area[ni][nj] < 1) continue;
        area[ni][nj] = 0;
        queue.push([ni, nj]);
        foodSize++;
      }
    }
    return foodSize;
  }

  // 탐색 실행
  let maxFoodSize = 0;
  for (const [i, j] of coords) {
    if (area[i][j] < 1) continue;
    maxFoodSize = Math.max(maxFoodSize, calculateFoodSize(i, j));
  }

  return maxFoodSize;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
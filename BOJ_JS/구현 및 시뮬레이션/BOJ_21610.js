/**
 * 제목 : 마법사 상어와 비바라기
 * 난이도 : 골드 5
 * 분류 : 시뮬레이션
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  // 0. 데이터 입력 및 초기화
  const [N, _] = convert(input[0]);
  const area = input.slice(1, N + 1).map(convert);
  const info = input.slice(N + 1,).map(convert);
  const delta1 = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]];
  const delta2 = [[-1, -1], [-1, 1], [1, -1], [1, 1]];
  let clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]];

  for (const [d, s] of info) {
    const isCloud = Array.from({ length: N }, () => {
      return Array.from({ length: N }, () => false);
    });

    // 1. 구름 이동
    for (let i=0; i<clouds.length; i++) {
      clouds[i][0] = (clouds[i][0] + s * delta1[d - 1][0] + N * 100) % N;
      clouds[i][1] = (clouds[i][1] + s * delta1[d - 1][1] + N * 100) % N;
      isCloud[clouds[i][0]][clouds[i][1]] = true;

      // 2. 물의 양 증가
      area[clouds[i][0]][clouds[i][1]]++;
    }

    // 3. 물 복사 버그
    for (const [r, c] of clouds) {
      for (const [dr, dc] of delta2) {
        const [nr, nc] = [r + dr, c + dc];
        if (nr < 0 || nc < 0 || nr >= N || nc >= N) continue;
        if (area[nr][nc] < 1) continue;
        area[r][c]++;
      }
    }

    // 4. 다음 구름 생성
    const nxtClouds = [];
    for (let r=0; r<N; r++) {
      for (let c=0; c<N; c++) {
        if (isCloud[r][c] || area[r][c] < 2) continue;
        area[r][c] -= 2;
        nxtClouds.push([r, c]);
      }
    }

    clouds = nxtClouds;
  }

  // 5. 최종 물의 양 합산
  let answer = 0;
  for (let r=0; r<N; r++) {
    for (let c=0; c<N; c++) {
      answer += area[r][c];
    }
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
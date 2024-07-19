/**
 * 제목 : 진우의 민트초코우유
 * 난이도 : 골드 5
 * 분류 : 백트랙킹, 브루트포스(그래프화)
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  // 데이터 입력
  const [N, M, H] = convert(input[0]);
  const area = input.slice(1).map(convert);

  // 그래프화를 위한 좌표 수집
  const node = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (area[i][j] === 0) continue;
      else if (area[i][j] === 2) node.push([i, j]);
      else node.unshift([i, j]);
    }
  }

  // 노드간의 거리를 계산하여 인접행렬 생성
  const adjM = Array.from({ length: node.length }, () => {
    return Array.from({ length: node.length }, () => 0);
  });
  for (let i = 0; i < node.length - 1; i++) {
    for (let j = i + 1; j < node.length; j++) {
      const distance = getDistance(node[i][0], node[i][1], node[j][0], node[j][1]);
      adjM[i][j] = distance;
      adjM[j][i] = distance;
    }
  }

  // 백트랙킹 탐색
  const visited = Array.from({ length: node.length }, () => false);
  visited[0] = true;
  let answer = 0;
  dfs(0, M, 0);

  return answer;

  // 노드간 거리 계산 함수
  function getDistance(i1, j1, i2, j2) {
    return Math.abs(i1 - i2) + Math.abs(j1 - j2);
  }

  // 백트랙킹 함수
  function dfs(v, hp, cnt) {
    // 우유 노드 방문시, 집으로 돌아갈 수 있으면 answer 갱신
    if (v !== 0 && hp - adjM[v][0] >= 0) {
      answer = Math.max(answer, cnt);
    }

    // 다음 우유 노드 탐색
    for (let w=1; w<node.length; w++) {
      // 방문했거나 현재 체력으로 갈 수 없다면 skip
      if (visited[w] || hp - adjM[v][w] < 0) continue;
      visited[w] = true;
      dfs(w, hp - adjM[v][w] + H, cnt + 1);
      visited[w] = false;
    }
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
// 그림

// [Main]
const solution = (input) => {
  // [1] 입력 초기화
  const [N, M] = input[0].split(" ").map((v) => +v);
  const graph = [];
  for (let i = 0; i < N; i++) {
    graph.push(input[i + 1].split(" ").map((v) => +v));
  }

  // [2] Sub-A 함수 실행 및 메인 함수 리턴
  return bfs();

  // [Sub]
  // [A] bfs 함수
  function bfs() {
    const visited = Array.from({ length: N }, () =>
        Array.from({ length: M }, () => false)
      );
    const delta = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const answer = [0, 0];  // answer = [그림의 개수, 그림의 최대 넓이]
    for (i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        // [A-1] 방문하지 않은 원소값이 1인 좌표 탐색
        if (graph[i][j] && !visited[i][j]) {
          answer[0]++;
          let areaCnt = 1;
          visited[i][j] = 1;
          let queue = [[i, j]];
          while (queue.length > 0) {
            const [vi, vj] = queue.shift();
            for (const [di, dj] of delta) {
              const [ni, nj] = [vi + di, vj + dj];
              if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
              if (!visited[ni][nj] && graph[ni][nj]) {
                visited[ni][nj] = true;
                areaCnt++;
                queue.push([ni, nj]);
              }
            }
          }
          answer[1] = Math.max(answer[1], areaCnt);
        }
      }
    }
    return answer.join('\n');
  };
};

// 데이터 입력 및 메인 함수 실행
const input = require("fs").readFileSync("./input.txt").toString().split("\n");
console.log(solution(input));
// 녹색 옷을 입은 애가 젤다지?

// [A] solution
const solution = (data) => {
  // 테스트 케이스 만큼 진행
  let idx = 0;
  const INF = 9 * 125 ** 2 + 1;
  let tc = 1;
  const delta = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  let ans = [];
  while (idx < data.length) {
    // [1] 데이터 입력 및 초기화
    const N = +data[idx++];
    if (!N) break;
    let cave = [];
    for (let i=0; i<N; i++) {
      cave.push(data[idx++].split(" ").map(v => +v));
    }
    ans.push(`Problem ${tc++}: ${bfs(N, cave)}`);
  }
  return ans.join("\n");

  function bfs(n, cave) {
    const visited = Array.from({length:n}, () => Array.from({length:n}, () => INF));
    visited[0][0] = cave[0][0];
    let q = [[0, 0]];
    while (q.length > 0) {
      let [vi, vj] = q.shift();
      if (vi === n - 1 && vj === n - 1) {
        continue;
      } else {
        for (let [di, dj] of delta) {
          let [ni, nj] = [vi + di, vj + dj];
          if (ni < 0 || nj < 0 || ni >= n || nj >= n) continue;
          if (visited[vi][vj] + cave[ni][nj] >= visited[ni][nj]) continue;
          visited[ni][nj] = visited[vi][vj] + cave[ni][nj];
          q.push([ni, nj]);
        }
      }
    }
    return visited[n - 1][n - 1];
  }
};

// [Main]
const main = () => {
  const input = require('fs').readFileSync('./input.txt').toString().split("\n");
  console.log(solution(input));
}

main();
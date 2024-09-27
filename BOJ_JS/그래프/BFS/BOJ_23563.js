/**
 * 제목 : 벽 타기
 * 난이도 : 골드 3
 * 분류 : 0-1 BFS, 덱
 */

const deque = () => {
  let head = 0;
  let rear = 0;
  const obj = {};

  const push = (x) => {
    obj[rear++] = x;
  };

  const shift = () => {
    const popData = obj[head];
    delete obj[head++];
    return popData;
  };

  const unshift = (x) => {
    obj[--head] = x;
  };

  const size = () => rear - head;

  return {
    push,
    unshift,
    shift,
    size,
  };
};

const solution = (input) => {
  // 데이터 입력 및 초기화
  const [H, W] = input[0].split(" ").map(Number);
  const grid = input.slice(1).map((v) => v.trim().split(""));
  const di = [1, -1, 0, 0];
  const dj = [0, 0, 1, -1];

  // 데이터 전처리
  // 시작, 끝지점 인덱스 저장
  // matrix => 벽타기 가능칸 = 0, 일반칸 = 1, 벽 = 2
  let si, sj, ei, ej;
  const matrix = Array.from(Array(H), () => Array(W).fill(1));
  for (let i = 0; i < H; i++) {
    for (let j = 0; j < W; j++) {
      if (grid[i][j] === "#") {
        matrix[i][j] = 2;
      } else {
        if (grid[i][j] === "S") {
          si = i;
          sj = j;
        } else if (grid[i][j] === "E") {
          ei = i;
          ej = j;
        }

        let ni, nj;
        for (let k = 0; k < 4; k++) {
          ni = i + di[k];
          nj = j + dj[k];
          if (!isValid(ni, nj)) continue;
          if (grid[ni][nj] === "#") {
            matrix[i][j] = 0;
            break;
          }
        }
      }
    }
  }

  // 0-1 BFS
  return bfs(si, sj, ei, ej);

  function isValid(i, j) {
    return i < 0 || j < 0 || i >= H || j >= W ? false : true;
  }

  function bfs(si, sj, ei, ej) {
    const visited = Array.from(Array(H), () => Array(W).fill(Infinity));
    const dq = deque();
    dq.push([si, sj]);
    let vi, vj;

    visited[si][sj] = 0;
    while (dq.size() > 0) {
      [vi, vj] = dq.shift();

      if (vi === ei && vj === ej) break;

      let ni, nj, d;
      for (let k = 0; k < 4; k++) {
        ni = vi + di[k];
        nj = vj + dj[k];
        if (!isValid(ni, nj)) continue;
        if (matrix[ni][nj] === 2) continue;
        d = matrix[vi][vj] || matrix[ni][nj] ? 1 : 0;
        if (visited[vi][vj] + d >= visited[ni][nj]) continue;
        visited[ni][nj] = visited[vi][vj] + d;
        if (d) {
          dq.push([ni, nj]);
        } else {
          dq.unshift([ni, nj]);
        }
      }
    }

    return visited[ei][ej];
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
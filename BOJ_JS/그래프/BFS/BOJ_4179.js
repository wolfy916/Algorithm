/**
 * 제목 : 불
 * 난이도 : 골드 3
 * 분류 : bfs
 */

class Node {
  constructor(value) {
    this.value = value;
    this.nextNode = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.rear = null;
    this.size = 0;
  }

  push(x) {
    const node = new Node(x);

    if (this.size < 1) {
      this.head = node;
    } else {
      this.rear.nextNode = node;
    }

    this.rear = node;

    this.size++;
  }

  pop() {
    const data = this.head.value;

    if (this.size === 1) {
      this.head = null;
      this.rear = null;
    } else {
      this.head = this.head.nextNode;
    }

    this.size--;

    return data;
  }
}

const solution = (input) => {
  const convert = {
    ".": 0,
    "#": 1,
    F: 2,
    J: 3,
  };

  const [N, M] = input[0].split(" ").map(Number);
  const maze = Array.from({ length: N }, (_, i) => {
    return input[i + 1].split("").map((v) => convert[v]);
  });

  const di = [-1, 1, 0, 0];
  const dj = [0, 0, -1, 1];
  
  const isInvalid = (i, j) => {
    return i < 0 || j < 0 || i >= N || j >= M;
  }
  const isEscape = (i, j) => {
    return i === 0 || j === 0 || i === N - 1 || j === M - 1;
  }

  let si, sj;
  const fireQueue = new Queue();
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (maze[i][j] < 2) continue;
      if (maze[i][j] === 2) {
        fireQueue.push([i, j]);
      } else {
        si = i;
        sj = j;
        maze[i][j] = 0;
      }
    }
  }

  const spreadFire = () => {
    const count = fireQueue.size;
    for (let i = 0; i < count; i++) {
      const [fi, fj] = fireQueue.pop();

      for (let k = 0; k < 4; k++) {
        const nfi = fi + di[k];
        const nfj = fj + dj[k];

        if (isInvalid(nfi, nfj)) continue;
        if (maze[nfi][nfj] === 0) {
          maze[nfi][nfj] = 2;
          fireQueue.push([nfi, nfj]);
        }
      }
    }
  };

  const timeLog = Array.from({ length: N }, () => {
    return Array(M).fill(Infinity)
  });
  timeLog[si][sj] = 0;

  const queue = new Queue();
  queue.push([si, sj, 0]);

  let answer = "IMPOSSIBLE";
  let spreadFireFlag = -1;

  while (queue.size > 0) {
    const [vi, vj, vt] = queue.pop();
    if (isEscape(vi, vj)) {
      answer = vt + 1;
      break;
    }

    if (spreadFireFlag < vt) {
      spreadFireFlag++;
      spreadFire();
    }

    for (let k = 0; k < 4; k++) {
      const ni = vi + di[k];
      const nj = vj + dj[k];

      if (isInvalid(ni, nj)) continue;
      if (maze[ni][nj] > 0) continue;
      if (timeLog[ni][nj] <= vt + 1) continue;

      timeLog[ni][nj] = vt + 1;
      queue.push([ni, nj, vt + 1]);
    }
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

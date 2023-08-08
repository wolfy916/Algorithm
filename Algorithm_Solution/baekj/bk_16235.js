// 나무 재테크

const solution = (input) => {
  // 입력 초기화
  const [N, M, K] = input[0].split(" ").map(v => +v);
  const area = Array.from({ length: N }, () => Array.from({ length: N }, () => 5));
  const trees = Array.from({ length: N }, () => Array.from({ length: N }, () => []));
  let A = [];
  for (let i = 1; i < N + 1; i++) {
    A.push(input[i].split(" ").map(v => +v));
  }
  let answer = 0
  for (let i = N + 1; i < M + N + 1; i++) {
    const [x, y, z] = input[i].split(" ").map(v => +v);
    trees[x-1][y-1].push(z);
    answer++;
  }
  const delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

  // 나무 어린순으로 배치
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (trees[i][j].length < 1) continue;
      trees[i][j].sort((a, b) => a - b)
    }
  }
  let year = 0;
  while (year < K) {
    year += 1;
    springAndSummer();
    fall();
    winter();
  }
  
  return trees.reduce((a, v) => a + v.reduce((a, v) => a + v.length, 0), 0);

  function springAndSummer() {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (trees[i][j].length < 1) continue;
        let k = 0;
        while (area[i][j]) {
          if (area[i][j] >= trees[i][j][k]) {
            area[i][j] -= trees[i][j][k];
            trees[i][j][k]++;
            k++;
          } else {
            break;
          };
        };
        // summer
        while (trees[i][j].length > k) {
          area[i][j] += ~~(trees[i][j].pop()/2);
        };
      };
    };
  };

  function fall() {
    let pos_tree = [];
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (trees[i][j].length < 1) continue;
        for (let k of trees[i][j]) {
          if (k % 5) continue;
          pos_tree.push([i, j]);
        };
      };
    };
    for (let [i, j] of pos_tree) {
      for (const [di, dj] of delta) {
        const [ni, nj] = [i + di, j + dj];
        if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
        trees[ni][nj].unshift(1);
      };
    };
  };

  function winter() {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        area[i][j] += A[i][j];
      };
    };
  };
};

const input = require("fs").readFileSync("./input.txt").toString().split('\n');
console.log(solution(input));
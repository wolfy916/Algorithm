/**
 * 제목 : 뱀
 * 난이도 : 골드 4
 * 분류 : 덱, 시뮬레이션
 */

const convert = (strArr) => strArr.split(" ").map(Number);

const deque = () => {
  const obj = {};
  let front = 0;
  let rear = 0;

  const push = (x) => {
    obj[rear++] = x;
  };

  const pop = () => {
    const popData = obj[rear];
    delete obj[rear--];
    return popData;
  };

  const shift = () => {
    const popData = obj[front];
    delete obj[front++];
    return popData;
  };

  const getFront = () => obj[front];

  const getRear = () => obj[rear - 1];

  return {
    push,
    pop,
    shift,
    getFront,
    getRear,
  };
};

const solution = (input) => {
  const N = Number(input[0]);
  const K = Number(input[1]);
  const apples = input.slice(2, K + 2).map(convert);
  const snakeInfo = input.slice(K + 3).map((v) => v.trim().split(" "));
  const board = Array.from({ length: N + 1 }, () => {
    return Array.from({ length: N + 1 }, () => 0);
  });
  const delta = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  const refC = { L: -1, D: 1 };
  let dir = 0;
  let answer = 0;
  let p = snakeInfo.length - 1;

  for (const [ai, aj] of apples) board[ai][aj] = 1;

  snakeInfo.forEach((v) => {
    v[0] = Number(v[0]);
  });

  snakeInfo.reverse();

  const snake = deque();
  snake.push([1, 1]);
  board[1][1] = 2;

  const checkMove = () => {
    const [i, j] = snake.getRear();
    const [ni, nj] = [i + delta[dir][0], j + delta[dir][1]];
    // 벽 충돌
    if (ni < 1 || ni > N || nj < 1 || nj > N) return [false, null, null];
    // 뱀의 몸 충돌
    const [fi, fj] = snake.getFront();
    if (board[ni][nj] === 2) return [false, null, null];
    return [true, ni, nj];
  };

  const move = (ni, nj) => {
    const [fi, fj] = snake.getFront();
    // 사과, 성장
    if (board[ni][nj] === 1) {
      board[ni][nj] = 2;
      snake.push([ni, nj]);
      // 빈 칸
    } else {
      board[fi][fj] = 0;
      board[ni][nj] = 2;
      snake.shift();
      snake.push([ni, nj]);
    }
  };

  const turn = (C) => {
    if (C === "L" && dir === 0) {
      dir = 3;
    } else {
      dir = (dir + refC[C]) % 4;
    }
  };

  while (true) {
    answer++;

    const [bool, ni, nj] = checkMove();

    if (bool) move(ni, nj);
    else break;

    if (p >= 0 && snakeInfo[p][0] === answer) {
      turn(snakeInfo[p][1]);
      p--;
    }
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
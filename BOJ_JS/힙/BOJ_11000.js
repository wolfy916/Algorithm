/**
 * 제목 : 강의실 배정
 * 난이도 : 골드 5
 * 분류 : 우선순위 큐, 정렬
 */

const minHeap = () => {
  const arr = [];

  const change = (i, j) => {
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }

  const bottomUp = () => {
    let cur = arr.length - 1;
    let par;
    while (cur > 0) {
      par = Math.floor((cur - 1) / 2);
      if (arr[par] > arr[cur]) {
        change(cur, par);
        cur = par;
      } else break;
    }
  }
  
  const push = (x) => {
    arr.push(x);
    bottomUp();
  }

  const topDown = () => {
    let cur = 0;
    let chd = cur * 2 + 1;
    while (chd < arr.length) {
      let sibling = chd + 1;
      if (sibling < arr.length && arr[chd] > arr[sibling]) {
        chd = sibling;
      }
      if (arr[cur] > arr[chd]) {
        change(cur, chd);
        cur = chd;
        chd = chd * 2 + 1;
      } else break;
    }
  }

  const updateTop = (x) => {
    arr[0] = x;
    topDown();
  }

  const getTop = () => arr[0];

  const getLength = () => arr.length;

  return {
    push,
    updateTop,
    getTop,
    getLength,
  }
}

const solution = (input) => {
  // 데이터 입력
  const N = Number(input[0]);
  const schedules = input.slice(1,).map(v => v.split(" ").map(Number));

  // 시작시간 기준 오름차순 정렬
  schedules.sort((a, b) => a[0] - b[0]);

  // 최소힙 생성
  const room = minHeap();
  room.push(schedules[0][1]); // 정렬 후, 첫번째 강의의 끝나는 시간 삽입

  // 메인 로직
  for (let i=1; i<N; i++) {
    const s = schedules[i][0];
    const e = schedules[i][1];
    // (최소 힙내에서 가장 빠르게 종료되는 강의 시간) <= (새로운 강의 시작 시간)
    // 위 조건을 충족하면 교실 수를 늘리지 않아야 하므로 updateTop
    if (room.getTop() <= s) room.updateTop(e);
    else room.push(e);
  }

  // 최소힙의 길이를 출력
  return room.getLength();
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
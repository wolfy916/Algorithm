// 센티와 마법의 뿅망치
// 파이썬의 소중함을 깨달았읍니다..

// 최대힙 구현
class MaxHeap{
  constructor() {
    this.lst = [0];
    this.cnt = 0;
  }
  // [1] 부모 노드 값
  parent(idx) {
    return this.lst[~~(idx/2)]
  }
  
  // [2] 왼쪽 자식 노드 값
  child1(idx) {
    return this.lst[idx * 2]
  }

  // [3] 오른쪽 자식 노드 값
  child2(idx) {
    return this.lst[idx * 2 + 1]
  }
  
  // [4] 원소값 위치 변경
  change(idx1, idx2) {
    [this.lst[idx1], this.lst[idx2]] = [this.lst[idx2], this.lst[idx1]];
  }

  // [5] 부모 노드와 비교하여 자식 노드 값을 올림
  up() {
    let idx = this.lst.length - 1;
    // 부모노드 값이 0이 아니고, 자식 노드값이 더 크다면
    while (this.parent(idx) !== 0 && this.parent(idx) < this.lst[idx]) {
      this.change(idx, ~~(idx/2));
      idx = ~~(idx/2);
    }
  }

  // [6] 자식노드와 비교하여 부모노드 값을 내림
  down() {
    let idx = 1;
    while (this.child1(idx) !== undefined
    && (this.child1(idx) > this.lst[idx] || this.child2(idx) > this.lst[idx])) {
      if (this.child2(idx) !== undefined && this.child2(idx) > this.lst[idx * 2]) {
        this.change(idx * 2 + 1, idx);
        idx = idx * 2 + 1;
      } else {
        this.change(idx * 2, idx);
        idx *= 2;
      }
    }
  }

  // [7] 최대힙 원소 추가
  add(value) {
    this.lst.push(value);
    this.up();
  }

  // [8] 루트 노드(가장 큰 값) 추출
  pop() {
    let value = this.lst[1];
    this.lst[1] = this.lst[this.lst.length - 1];
    this.lst.pop();
    this.down();
    return value;
  }

  // [9] 문제 조건에 맞는 망치질
  hammer(h) {
    let value = this.pop();
    if (value >= h && value > 1) {
      value = ~~(value/2);
      this.add(value);
      this.cnt++;
      return true;
    } else {
      this.add(value);
      return false;
    }
  }
}

// [A] solution
const solution = (data) => {
  // [1] 데이터 입력 및 초기화
  const [N, H, T] = data[0].split(" ").map(v => +v);
  let heights = new MaxHeap();
  for (let i=1; i<=N; i++) {
    heights.add(+data[i]);
  }
  
  // [2] 해머링
  while (heights.cnt < T) {
    if (!heights.hammer(H)) break;
  }

  // [3] 출력 포맷
  if (heights.lst[1] >= H || heights.cnt > T) {
    return `NO\n${heights.lst[1]}`;
  } else {
    return `YES\n${heights.cnt}`;
  }
};

// [Main]
const main = () => {
  const input = require('fs').readFileSync('./input.txt').toString().split("\n");
  console.log(solution(input));
}

main();
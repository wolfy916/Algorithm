class MinHeap {
  constructor() {
    // 힙을 저장할 배열
    this.heap = [];
  }

  // 힙의 크기를 반환하는 메서드
  size() {
    return this.heap.length;
  }

  // 두 값을 바꿔주는 메서드
  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  // 새로운 노드를 추가하는 메서드
  add(value) {
    this.heap.push(value); // 힙의 끝에 새로운 노드 추가
    this.bubbleUp(); // 새로운 값이 추가된 위치에서 bubbleUp() 수행
  }

  bubbleUp() {
    let index = this.heap.length - 1; // 새로운 노드가 추가된 위치
    let parentIdx = Math.floor((index - 1) / 2); // 부모 노드의 위치
    while (
      this.heap[parentIdx] && // 부모 노드가 존재하고
      this.heap[index] < this.heap[parentIdx] // 새로운 노드가 부모 노드보다 작은 경우
    ) {
      this.swap(index, parentIdx); // 두 노드의 값을 교체
      index = parentIdx; // 인덱스를 부모 노드의 인덱스로 변경
      parentIdx = Math.floor((index - 1) / 2); // 새로운 부모 노드의 인덱스 계산
    }
  }

  poll() {
    if (this.heap.length < 1) return 0;
    if (this.heap.length === 1) {
      return this.heap.pop(); // 힙의 크기가 1인 경우, 힙에서 값을 삭제하고 return
    }

    const value = this.heap[0]; // 힙의 최소값(루트 노드의 값)을 저장
    this.heap[0] = this.heap.pop(); // 힙의 끝에 있는 값을 루트 노드로 이동
    this.bubbleDown(); // 루트 노드에서 bubbleDown을 수행
    return value; // 삭제한 최소값 return
  }

  bubbleDown() {
    let index = 0; // 루트 노드의 index
    let leftIdx = index * 2 + 1; // 왼쪽 자식 노드의 index
    let rightIdx = index * 2 + 2; // 오른쪽 자식 노드의 index

    while (
      // 왼쪽 자식 노드가 존재 하면서 값이 루트 노드보다 작거나
      (this.heap[leftIdx] && this.heap[leftIdx][1] < this.heap[index][1]) ||
      // 오른쪽 자식 노드가 존재 하면서 값이 루트 노드보다 작은 경우
      (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[index][1])
    ) {
      let smallerIdx = leftIdx; // 왼쪽 자식 노드가 더 작다고 가정
      if (
        this.heap[rightIdx] &&
        this.heap[rightIdx][1] < this.heap[smallerIdx][1] // 오른쪽 자식 노드가 더 작다면
      ) {
        smallerIdx = rightIdx; // 오른쪽 자식 노드의 index로 변경
      }

      this.swap(index, smallerIdx); // 두 노드의 값을 교체
      index = smallerIdx; // index를 더 작은 값의 자식 노드의 index로 변경
      leftIdx = index * 2 + 1; // 왼쪽 자식 노드의 index 계산
      rightIdx = index * 2 + 2; // 오른쪽 자식 노드의 index 계산
    }
  }
}

const solution = (input) => {
  let line = 0;
  let number;
  const N = +input[line++];
  const minHeap = new MinHeap();
  for (let i = 0; i < N; i++) {
    number = +input[line++];
    if (number < 1) {
      console.log(minHeap.poll());
    } else {
      minHeap.add(number);
    }
  }
};

const input = require("fs").readFileSync("./input.txt").toString().split("\n");
solution(input);
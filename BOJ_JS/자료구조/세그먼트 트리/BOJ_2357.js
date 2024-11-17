/**
 * 제목 : 최솟값과 최댓값
 * 난이도 : 골드 1
 * 분류 : 세그먼트 트리
 */

class Node {
  constructor(minV, maxV) {
    this.minV = minV;
    this.maxV = maxV;
  }
}

class SegmentTree {
  constructor(n) {
    this.n = n;
    this.tree = Array.from(
      Array(this.n * 2 - 1),
      () => new Node(Infinity, -Infinity)
    );
  }

  getLeftChd(i) {
    return i * 2 + 1;
  }

  getRightChd(i) {
    return i * 2 + 2;
  }

  getParent(i) {
    return Math.floor((i - 1) / 2);
  }

  init(arr) {
    for (let i = 0; i < this.n; i++) {
      this.tree[this.n - 1 + i].minV = arr[i];
      this.tree[this.n - 1 + i].maxV = arr[i];
    }

    let leftChd, rightChd;
    for (let i = this.n - 2; i > -1; i--) {
      leftChd = this.getLeftChd(i);
      rightChd = this.getRightChd(i);
      this.tree[i].minV = Math.min(
        this.tree[leftChd].minV,
        this.tree[rightChd].minV
      );
      this.tree[i].maxV = Math.max(
        this.tree[leftChd].maxV,
        this.tree[rightChd].maxV
      );
    }
  }

  getValues(a, b) {
    a += this.n - 1;
    b += this.n - 1;

    if (a === b) {
      return `${this.tree[a].minV} ${this.tree[b].maxV}`;
    }

    let minV = Infinity;
    let maxV = -Infinity;

    while (a < b) {
      if (a % 2 === 0) {
        minV = Math.min(minV, this.tree[a].minV);
        maxV = Math.max(maxV, this.tree[a].maxV);
        a++;
      }

      if (b % 2 === 0) {
        minV = Math.min(minV, this.tree[b - 1].minV);
        maxV = Math.max(maxV, this.tree[b - 1].maxV);
        b--;
      }

      a = this.getParent(a);
      b = this.getParent(b);
    }

    return `${minV} ${maxV}`;
  }
}

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M] = convert(input[0]);
  const segmentTree = new SegmentTree(N);
  const arr = Array(N);
  const answer = [];

  for (let i = 1; i < N + 1; i++) {
    arr[i - 1] = Number(input[i]);
  }

  segmentTree.init(arr);

  let a, b;
  for (let i = N + 1; i < N + M + 1; i++) {
    [a, b] = convert(input[i]);
    answer.push(segmentTree.getValues(a - 1, b));
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));

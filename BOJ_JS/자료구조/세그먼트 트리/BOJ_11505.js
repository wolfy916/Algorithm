/**
 * 제목 : 구간 곱 구하기
 * 난이도 : 골드 1
 * 분류 : 세그먼트 트리
 */

class SegmentTree {
  constructor(arr) {
    this.n = arr.length;
    this.tree = Array(Math.pow(2, Math.ceil(Math.log2(this.n)) + 1)).fill(1n);
    this.mod = BigInt(1e9 + 7);

    const init = (start = 0, end = this.n - 1, index = 0) => {
      if (start === end) {
        this.tree[index] = BigInt(arr[start]);
        return this.tree[index];
      }

      const mid = Math.floor((start + end) / 2);
      const leftChd = init(start, mid, index * 2 + 1);
      const rightChd = init(mid + 1, end, index * 2 + 2);

      this.tree[index] = leftChd * rightChd % this.mod;

      return this.tree[index];
    };

    init();
  }

  getValue(a, b, start = 0, end = this.n - 1, index = 0) {
    if (b < start || end < a) return 1n;
    if (a <= start && end <= b) return this.tree[index];

    const mid = Math.floor((start + end) / 2);
    const leftChd = this.getValue(a, b, start, mid, index * 2 + 1);
    const rightChd = this.getValue(a, b, mid + 1, end, index * 2 + 2);

    return (leftChd * rightChd) % this.mod;
  }

  getIdx(b, start = 0, end = this.n - 1, index = 0) {
    if (b === start && start === end) return index;
    if (b < start || end < b) return 0;

    const mid = Math.floor((start + end) / 2);
    const leftChdIdx = this.getIdx(b, start, mid, index * 2 + 1);
    const rightChdIdx = this.getIdx(b, mid + 1, end, index * 2 + 2);

    return rightChdIdx + leftChdIdx;
  }

  update(b, c) {
    let cur = this.getIdx(b);
    this.tree[cur] = BigInt(c);
    while (cur > 0) {
      const par = Math.floor((cur - 1) / 2);
      const sibling = cur % 2 ? cur + 1 : cur - 1;
      this.tree[par] = this.tree[cur] * this.tree[sibling] % this.mod;
      cur = par;
    }
  }
}

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M, K] = convert(input[0]);

  const arr = Array(N);
  for (let i = 1; i < N + 1; i++) {
    arr[i - 1] = Number(input[i]);
  }

  const segmenTree = new SegmentTree(arr);
  const answer = [];
  for (let i = N + 1; i < N + M + K + 1; i++) {
    const [a, b, c] = convert(input[i]);
    if (a === 1) {
      segmenTree.update(b - 1, c);
    } else {
      answer.push(segmenTree.getValue(b - 1, c - 1));
    }
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
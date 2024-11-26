/**
 * 제목 : 최솟값
 * 난이도 : 골드 1
 * 분류 : 세그먼트 트리
 */

class SegmentTree {
  constructor(nums) {
    this.n = nums.length;
    this.tree = Array(this.n * 4).fill(0);

    const init = (start, end, index) => {
      if (start === end) {
        this.tree[index] = nums[start];
        return this.tree[index];
      }

      const leftChild = index * 2 + 1;
      const rightChild = index * 2 + 2;
      const mid = Math.floor((start + end) / 2);

      this.tree[index] = Math.min(
        init(start, mid, leftChild),
        init(mid + 1, end, rightChild),
      );

      return this.tree[index];
    }

    init(0, this.n - 1, 0);
  }

  getMinValue(left, right, start = 0, end = this.n - 1, index = 0) {
    if (left > end || right < start) return Infinity;
    if (left <= start && end <= right) return this.tree[index];

    const mid = Math.floor((start + end) / 2);
    const leftChildValue = this.getMinValue(left, right, start, mid, index * 2 + 1);
    const rightChildValue = this.getMinValue(left, right, mid + 1, end, index * 2 + 2);
    
    return Math.min(leftChildValue, rightChildValue);
  }
}

const solution = (input) => {
  const [N, M] = input[0].split(" ").map(Number);
  const nums = input.slice(1, N + 1).map(Number);
  const segmentTree = new SegmentTree(nums);
  const answer = [];

  for (let i=N + 1; i<N + M + 1; i++) {
    const [a, b] = input[i].split(" ").map(Number);
    answer.push(segmentTree.getMinValue(a - 1, b - 1));
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
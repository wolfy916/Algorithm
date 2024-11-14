/**
 * 제목 : 커피숍2
 * 난이도 : 골드 1
 * 분류 : 세그먼트 트리, 자료구조
 */

class SegmentTree {
  constructor(arr) {
    this.size = arr.length;
    this.tree = [];
    
    for (let i = 0; i < this.size; i++) {
      this.tree[this.size - 1 + i] = arr[i];
    }
    
    for (let i = this.size - 2; i > -1; i--) {
      this.tree[i] = this.tree[this.leftChildI(i)] + this.tree[this.rightChildI(i)];
    }
  }

  parentI(i) {
    return Math.floor((i - 1) / 2);
  }

  leftChildI(i) {
    return i * 2 + 1;
  }

  rightChildI(i) {
    return i * 2 + 2;
  }

  update(i, v) {
    i += this.size - 1;
    this.tree[i] = v;

    while (i > 0) {
      i = this.parentI(i);
      this.tree[i] = this.tree[this.leftChildI(i)] + this.tree[this.rightChildI(i)];
    }
  }

  query(l, r) {
    l += this.size - 1;
    r += this.size - 1;

    let sum = 0;
    while (l < r) {
      if (l % 2 === 0) {
        sum += this.tree[l];
        l++;
      }
      
      if (r % 2 === 0) {
        sum += this.tree[r - 1];
        r--;
      }

      l = this.parentI(l);
      r = this.parentI(r);
    }

    return sum;
  }
}

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, Q] = convert(input[0]);
  const nums = convert(input[1]);
  const segmentTree = new SegmentTree(nums);

  let x, y, a, b;
  const answer = [];
  for (let i = 2; i < Q + 2; i++) {
    [x, y, a, b] = convert(input[i]);
    answer.push(segmentTree.query(Math.min(x, y) - 1, Math.max(x, y)));
    segmentTree.update(a - 1, b);
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
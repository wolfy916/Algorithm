/**
 * 제목 : 수열과 쿼리 15
 * 난이도 : 골드 3
 * 분류 : 우선순위 큐, 세그먼트 트리
 */

class SegmentTree {
  constructor(arr) {
    this.arrSize = arr.length;
    this.tree = Array(this.arrSize * 2);

    for (let i = 0; i < this.arrSize; i++) {
      this.tree[this.arrSize + i] = [arr[i], i + 1];
    }

    for (let i = this.arrSize - 1; i > -1; i--) {
      this.swap(i);
    }
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

  getMinIdx() {
    return this.tree[0][1];
  }

  swap(par) {
    const leftChd = this.getLeftChd(par);
    const rightChd = this.getRightChd(par);

    const leftV = leftChd < this.arrSize * 2 ? this.tree[leftChd][0] : Infinity;
    const rightV = rightChd < this.arrSize * 2 ? this.tree[rightChd][0] : Infinity;

    if (leftV < rightV) {
      this.tree[par] = [...this.tree[leftChd]];
    } else if (rightV < leftV) {
      this.tree[par] = [...this.tree[rightChd]];
    } else {
      this.tree[par] = [this.tree[leftChd][0], Math.min(this.tree[leftChd][1], this.tree[rightChd][1])];
    }
  }

  update(idx, value) {
    let cur = idx + this.arrSize - 1;
    this.tree[cur][0] = value;
    let par;
    while (cur > 0) {
      par = this.getParent(cur);
      this.swap(par);
      cur = par;
    }
  }
}

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const N = Number(input.shift());
  const arr = convert(input.shift());
  const M = Number(input.shift());
  const segmentTree = new SegmentTree(arr);
  const answer = [];

  let query;
  for (let i = 0; i < M; i++) {
    query = convert(input[i]);
    if (query[0] === 1) {
      segmentTree.update(query[1], query[2]);
    } else {
      answer.push(segmentTree.getMinIdx());
    }
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
/**
 * 제목 : 특정한 최단 경로
 * 난이도 : 골드 4
 * 분류 : 데이크스트라
 */

// https://www.acmicpc.net/source/39827206 풀이 미쳤다;

const minHeap = () => {
  let arr = [];

  const bottomUp = () => {
    let cur = arr.length - 1;
    while (0 < cur) {
      let par = Math.floor((cur - 1) / 2);
      if (arr[par][1] > arr[cur][1]) {
        [arr[par], arr[cur]] = [arr[cur], arr[par]];
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
    let len = arr.length;
    while (true) {
      let left = 2 * cur + 1;
      let right = 2 * cur + 2;
      let smallest = cur;

      if (left < len && arr[left][1] < arr[smallest][1]) {
        smallest = left;
      }
      if (right < len && arr[right][1] < arr[smallest][1]) {
        smallest = right;
      }
      if (smallest !== cur) {
        [arr[cur], arr[smallest]] = [arr[smallest], arr[cur]];
        cur = smallest;
      } else break;
    }
  }

  const pop = () => {
    if (arr.length === 0) return null;
    if (arr.length === 1) return arr.pop();

    const top = arr[0];
    arr[0] = arr.pop();
    topDown();
    return top;
  }

  return {
    push,
    pop,
    arr,
  }
}

const convertToNumArr = (strArr) => strArr.split(" ").map(Number);

const solution = (input) => {
  const [N, E] = convertToNumArr(input[0]);
  const [edges, [v1, v2]] = [
    input.slice(1, E + 1).map(convertToNumArr),
    convertToNumArr(input[E + 1]),
  ];

  const graph = Array.from({ length: N + 1 }, () => []);
  for (const [a, b, c] of edges) {
    graph[a].push([b, c]);
    graph[b].push([a, c]);
  }

  const dijkstra = (s) => {
    const distance = Array.from({ length: N + 1 }, () => Infinity);    distance[s] = 0;
    const heap = minHeap();
    heap.push([s, 0]);

    while (heap.arr.length > 0) {
      const [v, vDist] = heap.pop();
      if (vDist > distance[v]) continue;

      for (const [n, nDist] of graph[v]) {
        if (distance[n] > distance[v] + nDist) {
          distance[n] = distance[v] + nDist;
          heap.push([n, distance[n]]);
        }
      }
    }

    return distance;
  }
  
  const distV1 = dijkstra(v1);
  const distV2 = dijkstra(v2);

  const path1 = distV1[1] + distV1[v2] + distV2[N];
  const path2 = distV2[1] + distV1[v2] + distV1[N];

  const answer = Math.min(path1, path2);

  return answer === Infinity ? -1 : answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
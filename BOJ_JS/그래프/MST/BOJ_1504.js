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
    let [cur, chd] = [0, 1];
    while (chd < arr.length) {
      let sibling = chd + 1;
      if (sibling < arr.length && arr[sibling][1] < arr[chd][1]) {
        chd = sibling;
      }
      if (arr[cur][1] < arr[chd][1]) {
        [arr[cur], arr[chd]] = [arr[chd], arr[cur]];
        cur = chd;
      } else break;
    }
  }

  const pop = () => {
    if (arr.length < 1) return null;
    if (arr.length < 2) return arr.pop();
    let popData;
    [popData, arr[0]] = [arr[0], arr.pop()];
    topDown();
    return popData;
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
      const [v, _] = heap.pop();
      for (const [nv, nw] of graph[v]) {
        if (distance[nv] > distance[v] + nw) {
          distance[nv] = distance[v] + nw;
          heap.push([nv, nw]);
        }
      }
    }
    return distance;
  }
  
  const distV1 = dijkstra(v1);
  const distV2 = dijkstra(v2);

  let answer = Infinity;
  const path1 = distV1[1] + distV1[v2] + distV2[N];
  const path2 = distV2[1] + distV1[v2] + distV1[N];

  answer = Math.min(answer, path1, path2);

  return answer === Infinity ? -1 : answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
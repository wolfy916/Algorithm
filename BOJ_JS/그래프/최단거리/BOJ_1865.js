/**
 * 제목 : 웜홀
 * 난이도 : 골드 3
 * 분류 : 최단 거리, 벨만-포드(음수 간선 순환 체크)
 */

const solution = (input) => {
  const convert = (strArr) => strArr.split(" ").map(Number);
  const answer = [];
  let idx = 0;
  let TC = Number(input[idx++]);

  while (TC--) {
    let [N, M, W] = convert(input[idx++]);
    const edges = []; // 간선 리스트 생성

    while (M--) {
      const [from, to, cost] = convert(input[idx++]);
      edges.push([from, to, cost]);
      edges.push([to, from, cost]);
    }

    while (W--) {
      const [from, to, cost] = convert(input[idx++]);
      edges.push([from, to, -cost]);
    }

    const result = bellmanFord(N, edges);
    answer.push(result);
  }

  return answer.join("\n");

  /**
   * 벨만-포드 알고리즘
   * 
   * 다익스트라와 같이 최단 경로 알고리즘으로 음수 가중치 간선이 존재할 때 사용된다.
   * 모든 간선을 순회하며 최단 거리 테이블 갱신을 시도할 때,
   * 음수 간선 순환이 존재한다면 갱신이 무한하게 이뤄질 것이므로
   * 모든 간선 순회를 (정점 개수 - 1)번 진행한 이후, 추가적인 갱신이 발생한다면 음수 간선 순환이 존재한다고 볼 수 있다.
   * 
   * 우선순위 큐 적용 다익스트라 : O(ElogV)
   * 벨만-포드 : O(VE)
   */
  function bellmanFord(N, edges) {
    // 최단 거리 테이블 INF값으로 초기화
    const INF = 1e9;
    const distance = Array.from({ length: N + 1 }, () => INF);
    distance[1] = 0; // 시작 노드 초기화
    let isUpdated;
    
    // (정점 개수)번 로직 수행
    for (let i = 0; i < N; i++) {
      isUpdated = false;
      // 매 반복마다 모든 간선을 순회하며 최단거리 테이블 갱신 시도
      for (const [from, to, cost] of edges) {
        if (distance[to] > distance[from] + cost) {
          // 마지막 회차에도 최단거리 테이블이 갱신된다면 음수 순환이 존재
          if (i === N - 1) return "YES";
          distance[to] = distance[from] + cost;
          isUpdated = true;
        }
      }

      // 이번 회차에 갱신되지 않는다면 다음 회차에도 갱신될 여지가 없음
      if (!isUpdated) return "NO";
    }
  };
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
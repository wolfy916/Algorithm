/**
 * 제목 : 왕위 계승
 * 난이도 : 골드 4
 * 분류 : 위상 정렬, 자료구조, 방향 비순환 그래프
 */

const solution = (input) => {
  const convert = (s) => s.split(" ").map(Number);
  const [N, M] = convert(input[0]);
  const founder = input[1].trim();
  const graph = {};

  graph[founder] = {
    value: 1,
    parents: [],
  }

  for (let i=2; i<N + 2; i++) {
    const [chd, par1, par2] = input[i].split(" ").map(v => v.trim());
    graph[chd] = {
      value: null,
      parents: [par1, par2],
    }
  }

  let answer = "";
  let maxV = 0;
  for (let i=N + 2; i<N + M + 2; i++) {
    const candidate = input[i].trim();
    const value = getValue(candidate);
    
    if (maxV < value) {
      answer = candidate;
      maxV = value;
    }
  }

  return answer;

  function getValue(name) {
    if (graph[name] === undefined) return 0;
    if (graph[name].value !== null) return graph[name].value;

    let value = 0;
    for (const par of graph[name].parents) {
      if (graph[par] === undefined) continue;
      value += getValue(par) / 2;
    }

    graph[name].value = value;

    return value;
  }
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
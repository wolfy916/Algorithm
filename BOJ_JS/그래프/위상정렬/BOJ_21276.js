/**
 * 제목 : 계보 복원가 호석
 * 난이도 : 골드 2
 * 분류 : ?
 */

class Person {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  get size() {
    return this.children.length;
  }

  get isRegistered() {
    return this.parent != null || this.children.length > 0;
  }
}

const solution = (input) => {
  const names = input[1].split(" ").sort();
  const M = Number(input[2]);

  const forefatherMap = new Map();
  const childMap = new Map();
  
  for (let i=3; i<M + 3; i++) {
    const [x, y] = input[i].split(" ");
    if (forefatherMap.get(x)) {
      forefatherMap.get(x).push(y);
    } else {
      forefatherMap.set(x, [y]);
    }

    if (childMap.get(y)) {
      childMap.get(y).push(x);
    } else {
      childMap.set(y, [x]);
    }
  }
  
  const trees = [];
  const nameToNodeMap = new Map(names.map(v => [v, new Person(v)]));

  const registerChild = (name, depth) => {
    const childNameList = childMap.get(name);
    if (childNameList === undefined) return;

    const personNode = nameToNodeMap.get(name);

    for (const childName of childNameList) {
      if (forefatherMap.get(childName).length > depth) continue;

      const childNode = nameToNodeMap.get(childName);
      personNode.children.push(childNode);
      
      registerChild(childName, depth + 1);
    }
  }

  for (const name of names) {
    if (forefatherMap.get(name)) continue;

    const person = nameToNodeMap.get(name);
    if (!person.isRegistered) trees.push(person);

    registerChild(name, 1);
  }

  const answer = [];

  answer.push(trees.length);
  answer.push(trees.map(v => v.name).join(" "));

  names.forEach(v => {
    const person = nameToNodeMap.get(v);
    const childNameList = person.children
      .map(v => v.name)
      .sort()
      .join(" ");
    answer.push(`${v} ${person.size} ${childNameList}`);
  });

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
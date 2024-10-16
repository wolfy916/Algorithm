/**
 * 제목 : 접두사 찾기
 * 난이도 : 실버 1
 * 분류 : 문자열, 트리, 트라이
 */

class Node {
  constructor(key) {
    this.key = key;
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.head = new Node(null);
  }

  insert(string) {
    let cur_node = this.head;

    for (const char of string) {
      if (cur_node.children[char] === undefined) {
        cur_node.children[char] = new Node(char);
      }
      cur_node = cur_node.children[char];
    }
  }

  search(string) {
    let cur_node = this.head;

    for (const char of string) {
      if (cur_node.children[char] !== undefined) {
        cur_node = cur_node.children[char];
      } else {
        return false;
      }
    }

    return true;
  }
}

const solution = (input) => {
  const [N, M] = input.shift().split(" ").map(Number);
  const trie = new Trie();

  for (let i = 0; i < N; i++) {
    trie.insert(input[i].trim());
  }

  let answer = M;
  for (let i = N; i < N + M; i++) {
    if (trie.search(input[i].trim())) continue;
    answer -= 1;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
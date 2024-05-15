// 접두사

const input = require("fs").readFileSync("./input.txt").toString().split("\n");

const N = +input[0];
const words = []
for (let i=1; i<=N; i++) {
  words.push(input[i].trim());
}
words.sort();
let cnt = 0;
for (let i=0; i<N - 1; i++) {
  if (words[i] <= words[i+1] && words[i+1].startsWith(words[i])) cnt++;
}
console.log(N - cnt);
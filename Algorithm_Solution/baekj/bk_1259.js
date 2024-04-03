const solution = (num) => {
  if (num === "0") return;
  console.log(num === num.split("").reverse().join("") ? "yes" : "no");
};

const input = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n");

for (let line of input) {
  solution(line.trim());
};

const solution = (input) => {
  const [N, A, _, B] = input.map((v) => v.split(" ").map((x) => Number(x)));

  const check = new Set();
  for (let i=0; i<N; i++) {
    check.add(A[i]);
  };

  for (let b of B) {
    console.log(check.has(b) ? 1 : 0);
  }
};

const input = require("fs").readFileSync("./input.txt").toString().trim().split("\n");

solution(input);
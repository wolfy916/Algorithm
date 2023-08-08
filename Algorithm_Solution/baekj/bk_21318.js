// 피아노 제조

// [A] solution
const solution = (data) => {
  // [1] 데이터 입력 및 초기화
  const N = +data[0];
  const musics = data[1].split(" ").map(v => +v);
  musics.unshift(0);
  const Q = +data[2];
  let qs = [];
  for (let i=0; i<Q; i++) {
    qs.push(data[i + 3].split(" ").map(v => +v));
  }

  // [2] 실수한 기록 누적합
  const mistakes = Array.from({length: N + 1}, () => 0);
  for (let i=1; i<N+1; i++) {
    if (musics[i-1] > musics[i]) mistakes[i]++;
    mistakes[i] += mistakes[i - 1];
  }

  // [3] 데이터 출력;
  let ans = [];
  for (let [x, y] of qs) {
    let mistake = mistakes[y] - mistakes[x];
    ans.push(mistake);
  }
  
  return ans.join("\n");
};

// [Main]
const main = () => {
  const input = require('fs').readFileSync('./input.txt').toString().split("\n");
  console.log(solution(input));
}

main();
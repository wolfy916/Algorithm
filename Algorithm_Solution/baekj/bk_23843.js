// 콘센트

// [A] solution
const solution = (data) => {
  // [1] 데이터 입력 및 초기화
  const [_, M] = data[0].split(" ").map(v => +v);
  const devices = data[1].split(" ").map(v => +v).sort((a, b) => b - a);
  let ans = 0;
  let charge = [];
  let idx = 0;
    
  // [2] 로직 실행
  while (idx < devices.length || charge.length > 0) {
    // [2-1] 콘센트에 꽂혀있는 기계가 있을때

    while (charge.length > 0) {
      if (charge[charge.length - 1] === ans) {
        charge.pop();
      } else {
        break;
      }
    }
    // [2-2] 콘센트를 최대한 사용하기
    while (charge.length < M && idx < devices.length) {
      charge.push(devices[idx] + ans);
      idx++;
    }
    // [2-3] 제일 충전길이가 짧은 
    if (charge.length > 0) {
      ans = charge[charge.length - 1];
    }
  }
  return ans;
};

// [Main]
const main = () => {
  const input = require('fs').readFileSync('./input.txt').toString().split("\n");
  console.log(solution(input));
}

main();
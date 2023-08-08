// 암호

const solution = (data) => {
  const string = Array.from(data[0].trim().split(""));
  const length = string.length;
  const pw = data[1].trim();
  let answer = 0;
  let cnt = 1;
  let value = length;
  while (cnt < pw.length) {
    answer += value % 900528;
    value *= length;
    answer %= 900528;
    cnt++;
  }

  for (let i=0; i<pw.length; i++) {
    let k = string.indexOf(pw[i]);
    let cnt = 0;
    let multiple = 1;
    while (cnt++ < pw.length - i - 1) {
        multiple *= length;
        multiple %= 900528;
    }
    answer += k * multiple % 900528;
    answer %= 900528;
  }

  return (answer + 1) % 900528;
}

const input = require('fs').readFileSync('./input.txt').toString().split('\n');
console.log(solution(input));
const stream = require('fs').createReadStream("./input.txt", { encoding: 'utf-8' });

let N = false;
let cnt = 0;
let max0 = max1 = max2 = 0;
let min0 = min1 = min2 = 0;
let num0 = num1 = num2 = 0;
let tmp0, tmp1;

stream.on('readable', () => {
  let chunk;
  while ((chunk = stream.read(1)) !== null) {
    if (chunk === '\r' || chunk === '\n' || chunk === " ") continue;
    if (N) {
      switch (cnt) {
        case 0:
          num0 = Number(chunk);
          break;
        case 1:
          num1 = Number(chunk);
          break;
        case 2:
          num2 = Number(chunk);

          tmp0 = max0;
          tmp1 = max1;

          max0 = Math.max(max0, max1) + num0;
          max1 = Math.max(tmp0, max1, max2) + num1;
          max2 = Math.max(tmp1, max2) + num2;

          tmp0 = min0;
          tmp1 = min1;

          min0 = Math.min(min0, min1) + num0;
          min1 = Math.min(tmp0, min1, min2) + num1;
          min2 = Math.min(tmp1, max2) + num2;
          break;
      }
      cnt = (cnt + 1) % 3;
    } else {
      N = true;
    }
  }
}).on('end', () => {
  console.log(Math.max(max0, max1, max2) + " " + Math.min(min0, min1, min2));
});
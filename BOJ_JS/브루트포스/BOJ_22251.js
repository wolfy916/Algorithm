/**
 * 제목 : 빌런 호석
 * 난이도 : 골드 5
 * 분류 : 브루트포스, 구현
 */

const solution = (input) => {
  // 데이터 입력
  const [N, K, P, X] = input[0].split(" ").map(Number);

  // 각 숫자별로 불이 들어오는 곳을 표기
  const display = Array.from({ length: 10 }, () => {
    return Array.from({ length: 7 }, () => true);
  }); 

  const isLightOff = [
    [3],
    [0, 1, 3, 4, 6],
    [1, 5],
    [1, 4],
    [0, 4, 6],
    [2, 4],
    [2],
    [1, 3, 4, 6],
    [],
    [4],
  ]

  for (let i=0; i<10; i++) {
    for (const j of isLightOff[i]) {
      display[i][j] = false;
    }
  }

  // 숫자의 변환에 대하여 반전 개수를 기록
  const ref = Array.from({ length: 10 }, () => {
    return Array.from({ length: 10 }, () => 0);
  });

  const reversalCount = (num1, num2) => {
    let cnt = 0;
    for (let i=0; i<7; i++) {
      if (display[num1][i] !== display[num2][i]) cnt++;
    }
    return cnt;
  }

  for (let i=0; i<9; i++) {
    for (let j=i+1; j<10; j++) {
      const cnt = reversalCount(i, j);
      ref[i][j] = cnt;
      ref[j][i] = cnt;
    }
  }

  // 숫자형 자료를 숫자를 원소로 갖는 1차원 배열로 변환하는 함수
  const convertToNumArr = (number) => number.toString().split("").map(Number);

  // 처음 층 번호 설정
  let startFloor = convertToNumArr(X);
  if (startFloor.length < K) startFloor = [...Array(K - startFloor.length).fill(0), ...startFloor];


  // 변환이 유효한지 검사하는 함수
  const isValid = (floorNum) => {
    let nxtFloor = convertToNumArr(floorNum);
    if (nxtFloor.length < K) nxtFloor = [...Array(K - nxtFloor.length).fill(0), ...nxtFloor];
    let cnt = 0;
    for (let i=0; i<K; i++) {
      cnt += ref[startFloor[i]][nxtFloor[i]];
    }
    return 0 < cnt && cnt <= P ? true : false;
  }

  // 유효한 변환 카운팅
  let answer = 0;
  for (let floor=1; floor<N + 1; floor++) {
    if (isValid(floor)) answer++;
  }

  return answer;
};

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(inputArr));
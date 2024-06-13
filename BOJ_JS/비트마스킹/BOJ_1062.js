/**
 * 제목 : 가르침
 * 난이도 : 골드 4
 * 분류 : (비트마스킹 or 백트랙킹), 브루트포스
 */

// 단순 백트랙킹 풀이(매우 느림)
const solution1 = (input) => {
  const [N, K] = input[0].split(" ").map(Number);
  if (K < 5) return 0;

  const words = input.slice(1,).map(v => v.trim());
  const alphabet = "bdefghjklmopqrsuvwxyz".split("");
  const isLearnChar = Array.from({ length: 26 }, () => false);
  let answer = 0;
  
  ['a', 'c', 'i', 'n', 't'].forEach(v => isLearnChar[v.charCodeAt() - 97] = true);

  // worst case : 50(= maxN) x 15(= maxWordLength)
  const countMatchedWord = () => {
    let count = 0;
    for (let i=0; i<N; i++) {
      let isPossible = true;
      for (const char of words[i]) {
        if (!isLearnChar[char.charCodeAt() - 97]) {
          isPossible = false;
          break;
        }
      }
      if (isPossible) count++;
    }
    return count;
  }

  // worst case : (352,716 : 21_C_(K-5)의 max값) * (50 * 15 : countMatchedWord) = 264,537,000
  // 2억 6천만인데 어떻게 통과된거지;
  const dfs = (learnCount, startIdx) => {
    if (learnCount >= K) {
      answer = Math.max(answer, countMatchedWord());
      return;
    }
    
    for (let i=startIdx; i<alphabet.length; i++) {
      isLearnChar[alphabet[i].charCodeAt() - 97] = true;
      dfs(learnCount + 1, i + 1);
      isLearnChar[alphabet[i].charCodeAt() - 97] = false;
    }
  }

  dfs(5, 0);

  return answer;
};

// 비트마스킹 풀이
const solution2 = (input) => {
  const [N, K] = input[0].split(" ").map(Number);
  if (K < 5) return 0;

  const words = []; // 단어들을 이진수로 변환해서 넣을꺼임

  // 0b10000010000100000101
  //   ^     ^    ^     ^ ^
  //   t     n    i     c a
  // a, c, i, n, t를 포함한 이진수 basic
  let basic = 0b10000010000100000101;
  let answer = 0;

  // 단어 순회
  for (let i=0; i<N; i++) {
    let word = input[i + 1].trim();
    
    // 각 단어의 알파벳을 이진수로 변환하여 추가
    let binV = basic;
    // j 범위 => 앞 4자리, 뒤 4자리 볼 필요없음 (basic에 이미 추가해놓았기 떄문)
    for (let j=4; j<word.length-4; j++) {
      // 예시) word.charAt(j)가 'd'라고 하면
      // idx = 'd'.charCodeAt()(= 100) - 97 = 3
      // (charCodeAt은 아스키 코드값을 반환, 97은 'a'의 아스키 코드값)
      let idx = word.charAt(j).charCodeAt() - 97;

      // 1 << idx : 1을 idx만큼 왼쪽으로 시프트시킴.
      // 1의 이진수는 0b1인데, idx(= 3)만큼 왼쪽으로 시프트시키면 0b1000(= 8)
      // binV |= 0b1000 : binV 와 0b1000의 OR 연산(합집합) 후, 할당
      // (basic | 0b1000일 경우, 0b10000010000100001101으로 알파벳 a, c, d, i, n, t를 포함했다는 의미하는 이진수로 사용)
      binV |= 1 << idx;
    }

    // 각 단어를 알파벳 포함 여부 확인을 위한 이진수로 변환
    words.push(binV);
  }

  // 비트연산의 시간복잡도는 O(1)이므로
  // checked 함수의 시간복잡도는 O(N)
  const checked = (learned) => {
    let count = 0;
    for (let i=0; i<N; i++) {
      // & : AND연산(교집합)의 결과가 단어와 일치한다면 읽을 수 있는 단어
      if ((words[i] & learned) == words[i]) count++;
    }
    answer = Math.max(answer, count);
  }
 
  // 재귀 함수는 재귀 깊이가 시간 복잡도의 영향을 미침
  // checked 함수(= O(N))를 고려하고,
  // 최대 재귀 깊이는 K - 5이며,
  // 최대 재귀 분기는 2개이므로,
  // select 함수의 시간복잡도는 O(2^(K - 5) * N)로
  // 최악의 경우 2^21 * 50 = 104,857,600
  // 읭? 1억이 넘어가는데..?
  const select = (index, count, learned) => {
    // K만큼 배웠다면 체킹
    if (count === K) {
      checked(learned);
      return;
    }

    // 인덱스가 알파벳 수를 초과한다면 리턴
    if (index == 26) return;

    // 해당 인덱스의 알파벳을 배우지 않고 재귀
    select(index + 1, count, learned);

    // 해당 알파벳을 배우지 않았다면 배우고 재귀
    if ((learned & (1 << index)) == 0) {
      select(index + 1, count + 1, learned | (1 << index));
    }
  }

  select(0, 5, basic); // select(index, count, learned)

  return answer;
}

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputArr = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution2(inputArr));
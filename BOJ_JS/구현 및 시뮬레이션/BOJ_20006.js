/**
 * 제목 : 랭킹전 대기열
 * 난이도 : 실버 2
 * 분류 : 구현, 시뮬레이션
 */

// const a = [[2, "c"], [1, "a"]];
// 배열이 위와 같을때 문자열 기준 사전순으로 정렬하기 위해
// a.sort((a, b) => a[1] - b[1]);
// 위와 같은 sort를 작성해봤지만 기능하지 않았음
// a.sort((a, b) => a[1].localeCompare(b[1]))을 사용해야함

class Room {
  constructor(level, nickname, m) {
    this.players = [[level, nickname]];
    this.isStarted = m === 1 ? true : false;
    this.enterLimit = level;
    this.m = m;
  }

  isReadyToStart() {
    return this.players.length === this.m ? true : false;
  }

  isValidLevel(level) {
    if (level < this.enterLimit - 10 || this.enterLimit + 10 < level)
      return false;
    else return true;
  }

  enterPlayer(level, nickname) {
    if (this.isStarted) return false;
    if (this.isValidLevel(level)) {
      this.players.push([level, nickname]);
      if (this.isReadyToStart()) {
        this.isStarted = true;
      }
      return true;
    } else {
      return false;
    }
  }
}

const solution = (input) => {
  const [P, M] = input[0].split(" ").map(Number);
  const roomList = [];

  // 플레이어 순회
  let level, nickname, isEnter;
  for (let i = 1; i < P + 1; i++) {
    // 플레이어 데이터 초기화
    [level, nickname] = input[i].split(" ");
    level = Number(level);
    nickname = nickname.trim();

    // 생성되있는 방 순회
    for (let j = 0; j < roomList.length; j++) {
      isEnter = roomList[j].enterPlayer(level, nickname);
      if (isEnter) break; // 입장에 성공하면 순회 종료
    }

    // 입장을 못했을 경우, 방 생성
    if (!isEnter) roomList.push(new Room(level, nickname, M));
  }

  // 출력
  const answer = [];
  let room;
  for (let i = 0; i < roomList.length; i++) {
    room = roomList[i];
    answer.push(room.isStarted ? "Started!" : "Waiting!");
    room.players.sort((a, b) => a[1].localeCompare(b[1]));
    for (const player of room.players) {
      answer.push(player.join(" "));
    }
  }

  return answer.join("\n");
};

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
console.log(solution(input));
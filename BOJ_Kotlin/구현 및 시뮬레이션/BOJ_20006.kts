// 랭킹전 대기열
// 분류 : 구현 및 시뮬레이션

class Game(roomSize: Int) {
    val roomList: MutableList<Room> = mutableListOf()
    var addRoomIdx: Int = 0
    val roomSize: Int = roomSize

    // 새로운 방을 생성
    fun createRoom(player: Player) {
        roomList.add(Room(roomSize))
        roomList[addRoomIdx].enterPlayer(player)
        addRoomIdx++
    }

    // 플레이어를 대기중인 방에 넣는 함수
    fun waitingPlayer(player: Player) {
        var isSuccess: Boolean = false

        for (room in roomList) {
            isSuccess = room.tryEnterPlayer(player)
            if (isSuccess) break
        }

        // 대기중인 방이 없을 경우, 새로운 방을 생성
        if (!isSuccess) createRoom(player)

    }

    // 게임의 전체 상태를 출력하는 함수
    fun printGameState() {
        for (room in roomList) {
            println(room.roomState)
            room.playerList
                .sortedBy { it.name }
                .let {
                    for (player in it) {
                        println("${player.level} ${player.name}")
                    }
                }
        }
    }
}

class Room(roomSize: Int) {
    val roomSize: Int = roomSize
    val playerList: MutableList<Player> = mutableListOf()
    var numberOfEnterPlayer = 0
    var enterLevelLimit: Int? = null
    var roomState: String = "Waiting!"

    // 방의 입장 레벨 조건을 확인하는 함수
    fun isValidLevel(playerLevel: Int): Boolean {
        if (enterLevelLimit == null) return true
        if (playerLevel < enterLevelLimit!! - 10 || playerLevel > enterLevelLimit!! + 10) {
            return false
        } else {
            return true
        }
    }

    // 플레이어를 방에 입장시키는 함수
    fun enterPlayer(player: Player) {
        playerList.add(player)
        numberOfEnterPlayer++
        if (numberOfEnterPlayer == 1) {
            enterLevelLimit = player.level
        }
        if (numberOfEnterPlayer == roomSize) {
            roomState = "Started!"
        }
    }

    // 플레이어가 방에 입장할 수 있는지 확인하는 함수
    fun tryEnterPlayer(player: Player): Boolean {
        if (isValidLevel(player.level)) {
            if (roomSize >= numberOfEnterPlayer + 1) {
                enterPlayer(player)
                return true
            }
        }
        return false
    }
}

class Player(playerLevel: Int, playerName: String) {
    var level: Int = playerLevel
    var name: String = playerName
}


fun main() = with(System.`in`.bufferedReader()) {
    // 플레이어 수와 방
    val (numberOfPlayer, roomSize) = readLine().split(" ").map{ it.toInt() }

    // 게임 생성
    val game = Game(roomSize)

    // 플레이어 입장
    for (i in 1..numberOfPlayer) {
        val (l, n) = readLine().split(" ")
        val playerLevel = l.toInt()
        val playerName = n
        val player = Player(playerLevel, playerName)
        game.waitingPlayer(player)
    }

    // 게임 결과 출력
    game.printGameState()
}

main()
function findQueens(n) {
  const di = [-1, -1, 0, 1, 1, 1, 0, -1]
  const dj = [0, 1, 1, 1, 0, -1, -1, -1]

  let answer = 0
  let zeroList = []
  for (let i=0; i<n; i++){
    zeroList.push(0)
  }

  for (let i=0; i<n; i++) {
    let chess = []
    for (let j=0; j<n; j++) {
      chess.push(zeroList)
    }
    check(0, i, 1)
  }

  function promising(v_i, v_j) {
    for (let i=1; i<n; i++) {
      for (let j=0; j<8; i++) {
        let ni = v_i+di[j]*i
        let nj = v_j+dj[j]*i
        if (0 <= ni < n && 0 <= nj < n && chess[ni][nj] == 1) {
          return false
        }
      }
    }
    chess[v_i][v_j] = 1
    return true
  }

  function check(v_i, v_j, q) {
    if (promising(v_i, v_j)) {
      if (q == n) {
        cnt ++
      } else {
        for (let i=0; i<n; i++) {
          check(v_i+1, i, q+1)
          chess[v_i+1][i] = 0
        }
      }
    }
  }
	return answer
}

console.log(findQueens(4)) // 2
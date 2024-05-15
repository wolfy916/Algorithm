# 드래곤 커브
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 드래곤 커브 생성 함수
def make_curve(coords, cur_g, g):
    # 원하는 세대를 생성하면 종료
    if cur_g == g:
        return coords
    # 끝점 기준 회전
    ei, ej = coords.pop()
    rot_coords = []
    # 시작 좌표(coords[0])가 마지막 차례가 되는 순서로 회전
    for idx in range(len(coords) - 1, -1, -1):
        i, j = coords[idx]
        di, dj = ei - i, ej - j
        ni, nj = ei - dj, ej + di
        rot_coords.append((ni, nj))
    return make_curve(coords + [(ei, ej)] + rot_coords, cur_g + 1, g)

# [C] 메인 로직 함수
def solution(curves):
    # 드래곤 커브들을 평면에 표기
    grid = [[False] * 101 for _ in range(101)]
    delta1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for x, y, d, g in curves:
        dy, dx = delta1[d]
        ny, nx = y + dy, x + dx
        coords = make_curve([(y, x), (ny, nx)], 0, g)
        for i, j in coords:
            if i < 0 or j < 0 or i >= 101 or j >= 101: continue
            grid[i][j] = True

    # 사각형 갯수 카운팅
    answer = 0
    delta2 = [(0, 0), (1, 0), (0, 1), (1, 1)]
    for i in range(100):
        for j in range(100):
            for di, dj in delta2:
                ni, nj = i + di, j + dj
                if not grid[ni][nj]: break
            else:
                answer += 1
    return answer

# [main]
if __name__ == '__main__':
    N = int(input())
    curves = [tuple(map(int, input().split())) for _ in range(N)]
    print(solution(curves))

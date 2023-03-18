# 베스트 앨범
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    # 장르별 노래들 dict, 장르별 play 횟수 dict 생성
    genre_songs, genre_plays = dict(), dict()
    for idx, genre in enumerate(genres):
        play = plays[idx]
        if genre not in genre_songs.keys():
            genre_songs[genre] = [(idx, play)]
            genre_plays[genre] = play
        else:
            genre_songs[genre].append((idx, play))
            genre_plays[genre] += play

    # (장르, 플레이횟수)를 원소로 갖는 list 생성
    genre_plays_lst = []
    for genre in genre_songs.keys():
        genre_plays_lst.append((genre, genre_plays[genre]))

    # 총 플레이횟수로 장르 내림차순 정렬
    genre_plays_lst.sort(key=lambda x: x[1], reverse=True)

    # 장르별 수록곡들의 개별 플레이 횟수로 수록곡 내림차순 정렬하여 곡 선택
    for genre, total_play in genre_plays_lst:
        temp_lst = sorted(genre_songs[genre])
        temp_lst.sort(key=lambda x: x[1], reverse=True)
        for idx, play in temp_lst[:2]:
            answer.append(idx)

    return answer

print(solution(genres, plays))
# 화물 도크

for tc in range(1, int(input()) + 1):

    # [1]
    num_of_meetings = int(input())
    meeting_list = []

    # [2]
    for i in range(num_of_meetings):
        start, end = input().split()
        meeting_dict = {'start_time': int(start), 'end_time': int(end), 'meeting_hour': int(end) - int(start)}
        meeting_list.append(meeting_dict)

    # [3]
    meeting_list = sorted(meeting_list, key=lambda x: x['start_time'])
    meeting_list = sorted(meeting_list, key=lambda x: x['end_time'])

    # [4]
    end_time = meeting_list[0]['end_time']
    count = 1
    for j in range(1, len(meeting_list)):
        if end_time <= meeting_list[j]['start_time']:
            end_time = meeting_list[j]['end_time']
            count += 1

    print(f'#{tc} {count}')
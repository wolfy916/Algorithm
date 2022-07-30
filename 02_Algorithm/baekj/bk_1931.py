''' 
-백준 회의실 배정-

한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

-입력-
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 
시작 시간과 끝나는 시간은 2**31-1보다 작거나 같은 자연수 또는 0이다.

-출력-
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
'''

# 메모리 66736 KB, 시간 5780 ms

# [1]: 회의 수와 각 회의를 입력받기 위한 변수 선언
# [2]: 반복문으로 각 회의들의 시작, 종료 시간을 입력받고, 빈 list에 모두 append
# [3]: 완성된 list를 시작시간으로 1번, 종료시간으로 1번씩 정렬
# [4]: end_time = (list의 0번째 요소의 end_time 값), count = 1 할당하며 변수 선언
# [5]: list의 1번째 요소의 start_time 값을 end_time 변수와 비교, 충족한다면 end_time 변수 업데이트 및 count += 1

# [1]
num_of_meetings = int(input())
meeting_list =  []

# [2]
for i in range(num_of_meetings):
    start, end = input().split()
    meeting_dict = {'start_time': int(start), 'end_time': int(end), 'meeting_hour': int(end)-int(start)}
    meeting_list.append(meeting_dict)

# [3]
meeting_list = sorted(meeting_list, key=lambda x:x['start_time'])
meeting_list = sorted(meeting_list, key=lambda x:x['end_time'])

# [4]
end_time = meeting_list[0]['end_time']
count = 1

# [5]
for j in range(1, len(meeting_list)):
    if end_time <= meeting_list[j]['start_time']:
        end_time = meeting_list[j]['end_time']
        count += 1

print(count)
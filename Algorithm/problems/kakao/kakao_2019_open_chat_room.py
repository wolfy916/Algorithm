# 오븐채팅방

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"];

def solution(record):
    answer = []
    user = dict()
    message = ["님이 들어왔습니다.", "님이 나갔습니다."]
    chat_log = []
    for item in record:
        log, id, *name = item.split(" ")
        if log == "Enter":
            chat_log.append((0, id))
            user[id] = name
        elif log == "Leave":
            chat_log.append((1, id))
        else:
            user[id] = name
    for message_idx, id in chat_log:
        answer.append(user[id][0] + message[message_idx])
    return answer

print(solution(record))
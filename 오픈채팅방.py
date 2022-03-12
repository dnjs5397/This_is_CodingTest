record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

idmap = {}
answer = []
for i in record:
    tmplist = i.split()
    cmd = tmplist[0]
    if cmd == 'Enter' or cmd == 'Change':
        id = tmplist[1]
        name = tmplist[2]
        idmap[id] = name

for i in record:
    tmplist = i.split()
    cmd = tmplist[0]
    if cmd == 'Enter':
        id = tmplist[1]
        answer.append(idmap[id] + '님이 들어왔습니다.')
    elif cmd == 'Leave':
        id = tmplist[1]
        answer.append(idmap[id] + '님이 나갔습니다.')
        
print(answer)
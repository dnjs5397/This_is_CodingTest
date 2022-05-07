survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
test = {}
test['R'] = 0
test['T'] = 0
test['C'] = 0
test['F'] = 0
test['J'] = 0
test['M'] = 0
test['A'] = 0
test['N'] = 0
for i in range(len(survey)):
    if choices[i] == 4:
        continue
    elif choices[i] == 1:
        test[survey[i][0]] += 3
    elif choices[i] == 2:
        test[survey[i][0]] += 2
    elif choices[i] == 3:
        test[survey[i][0]] += 1
    else:
        test[survey[i][1]] += (choices[i]-4)

answer = ''
if test['R'] > test['T']:
    answer += 'R'
elif test['R'] < test['T']:
    answer += 'T'
else:
    answer += 'R'

if test['C'] > test['F']:
    answer += 'C'
elif test['C'] < test['F']:
    answer += 'F'
else:
    answer += 'C'
    
if test['J'] > test['M']:
    answer += 'J'
elif test['J'] < test['M']:
    answer += 'M'
else:
    answer += 'J'
    
if test['A'] > test['N']:
    answer += 'A'
elif test['A'] < test['N']:
    answer += 'N'
else:
    answer += 'A'

print(answer)
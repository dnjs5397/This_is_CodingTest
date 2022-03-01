s = "abcabcabcabcdededededede"
len_count_num = len(s)
    

for i in range(1, len(s)//2 + 1):
    pos = 0
    length = len(s)
    while (pos + i <= len(s)):
        tmp = s[pos:pos+i]
        count = 0
        pos += i
        while(pos + i <= len(s)):
            if (tmp == s[pos:pos+i]):
                count += 1
                pos += i
            else:
                break
        if count > 0:
            length -= count * i
        
        if count < 9:
            length += 1
        elif count < 99:
            length += 2
        elif count < 999:
            length += 3
        else:
            length += 4
        
    len_count_num = min(len_count_num, length)
    
print(len_count_num)
                



































# for i in range(1, len(s)//2+1):
#     pos = 0
#     length = len(s)
    
#     while(pos + i <= len(s)):
#         unit = s[pos:pos+i]
#         pos += i
        
#         cnt = 0
#         while (pos + i <= len(s)):
#             if unit == s[pos:pos+i]:
#                 cnt += 1
#                 pos += i
#             else:
#                 break
#         if cnt > 0:
#             length -= i * cnt
            
#             if cnt < 9:
#                 length += 1
#             elif cnt < 99:
#                 length += 2
#             elif cnt < 999:
#                 length += 3
#             else:
#                 length += 4
    
#     len_count_num = min(len_count_num, length)
    
# print(len_count_num)
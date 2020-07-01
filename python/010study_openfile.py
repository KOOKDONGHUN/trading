# C:\Users\bitcamp\Desktop
f = open('c:/Users/bitcamp/Desktop/buy_list.txt', 'rt',encoding='utf-8')
# cp949 안됨 

lines = f.readlines()
print(lines)
f.close()

for line in lines:
    print(line,end='')
print()

for line in lines:
    nline = line.split('\n')
    # print(nline)
    nline = nline[0]
    print(nline)

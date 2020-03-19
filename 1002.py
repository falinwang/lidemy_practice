import sys
# str = sys.stdin.readlines()
for line in sys.stdin:
    temp = line.split()
    if int(temp[0]) == 0 and int(temp[1]) == 0:
        # print('bye')
        break
    if int(temp[0]) > int(temp[1]):
        print(int(temp[0]))
    else:
        print(int(temp[1]))

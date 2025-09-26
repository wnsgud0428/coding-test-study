from collections import deque

dic = {}
dic['apple'] = 3
dic['banana'] = 1
dic['pear'] = 5

print(dic)

print(sorted(dic.items(), key = lambda x: x[0]))
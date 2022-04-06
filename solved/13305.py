N = int(input())  # 도시개수
road_lens = list(map(int, input().split()))
prices = list(map(int, input().split()))

# print(N, road_lens, prices)

min_index = 0
for i in range(1, len(road_lens)):
    if prices[min_index] > prices[i]:  # 오른쪽의 주유소값이 더 작은경우
        min_index = i
    else:  # 오른쪽의 주유소값이 같거나 더 큰경우
        road_lens[min_index] += road_lens[i]
        road_lens[i] = 0

# print(road_lens)

sum = 0
for i in range(len(road_lens)):
    sum += prices[i] * road_lens[i]

print(sum)

"""핵심
각 도시 주유소의 기름값을 담고있는 prices리스트는 내림차순으로 되어야 한다!
즉, 지나쳐왔던 도시들 중 기름값이 최소인 지점의 index를 저장시켜놓고, 문제를 풀면 된다.

예를 들어 각 도시의 주유소 값이 [5, 2, 4, 1] 이면 
값이 4인 곳(index:2)에서는 주유를 할 필요가 없으므로 [5,2,2,1] 과 같은 내림차순의 형태로 생각하면 편리하다.
내 코드에서는 prices리스트를 건들지 않고, 도시간의 거리인 road_lens 리스트에서 해당하는 값(index:2)을 0으로 맞춰 주었다.([2,3,1] -> [2,4,0])
개념적으로 기름값이 2~1인 지점을 하나로 묵었다고 생각하면 편하다. [5,2,4,1] -> [5,2,1]
"""

def print2DList(arr):
    for ar in arr:
        for a in ar:
            if a == 1:
                print("*",end="")
            else:
                print(" ",end="")
        print()


N = int(input())
stars = [[0 for i in range(4*(N-1)+1)] for i in range(4*(N-1)+1)]

mid_index = (N-1)*2
for stage in range(1,N+1): # i -> 1~N
    #위
    stars[mid_index-2*(stage-1)][mid_index] = 1
    for i in range((stage-1)*2): #오른쪽 채우기
        stars[mid_index-2*(stage-1)][mid_index+(i+1)] = 1
    for i in range((stage-1)*2): #왼쪽 채우기, 1씩 감소
        stars[mid_index-2*(stage-1)][mid_index-(i+1)] = 1
    #왼쪽
    stars[mid_index][mid_index-2*(stage-1)] = 1
    for i in range((stage-1)*2): #오른쪽 채우기
        stars[mid_index+(i+1)][mid_index-2*(stage-1)] = 1
    for i in range((stage-1)*2): #왼쪽 채우기, 1씩 감소
        stars[mid_index-(i+1)][mid_index-2*(stage-1)] = 1
    #아래
    stars[mid_index+2*(stage-1)][mid_index] = 1
    for i in range((stage-1)*2): #오른쪽 채우기
        stars[mid_index+2*(stage-1)][mid_index+(i+1)] = 1
    for i in range((stage-1)*2): #왼쪽 채우기, 1씩 감소
        stars[mid_index+2*(stage-1)][mid_index-(i+1)] = 1
    #오른쪽
    stars[mid_index][mid_index+2*(stage-1)] = 1
    for i in range((stage-1)*2): #오른쪽 채우기
        stars[mid_index+(i+1)][mid_index+2*(stage-1)] = 1
    for i in range((stage-1)*2): #왼쪽 채우기, 1씩 감소
        stars[mid_index-(i+1)][mid_index+2*(stage-1)] = 1
# print(stars)
print2DList(stars)



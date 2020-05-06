if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
print(arr)
array = list(arr)
print(array)
max_num = -100
i,j = 0,0
for i in range(n):
    if(array[i] > max_num):
        max_num = array[i]

second_max = -100
for j in range(n):
    if (array[j] > second_max) and (array[j] < max_num):
        second_max = array[j]

print(second_max)
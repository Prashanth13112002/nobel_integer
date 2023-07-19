def Noble_Integer(arr):
    arr.sort(reverse=True)
    count=[0]
    last_value=arr[0]
    current_count=0
    for i in range(1,len(arr)):
        if last_value!=arr[i]:
            count.append(i)
            current_count=i
        else:
            count.append(current_count)
    for i in range(len(arr)):
        if arr[i]==count[i]:
            return 1
    return -1
a=list(map(int,input().split()))
print(Noble_Integer(a))
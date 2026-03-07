arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
n = 10
# 감소일때도 "도착점은 절대 포함하지 않고 멈춤"


# 1.선택정렬 - O(N^2)
def select(arr, n):
    # arr[0]~arr[i] 까지만 보기
    for i in range(n - 1, 0, -1):
        mxidx = 0
        for j in range(1, i + 1):
            if arr[mxidx] < arr[j]:
                mxidx = j

        arr[mxidx], arr[i] = arr[i], arr[mxidx]


select(arr.copy(), n)
print(arr)


# 2. 버블정렬-O(N^2)
def bubble(arr, n):
    # 앞 값이 더크면 바꾸기.
    # (0,1)-(1,2)...(N-2,N-1) 스왑

    for j in range(n - 1, 0, -1):
        # (0,1)-(1,2)-....- (j-1,j) 스왑 포함
        # 마지막 : j=1이면 arr[0],arr[1] 비교
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                # 스왑
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr2 = [2, 13, 6, 4, -2]
n = 5

bubble(arr2, n)
print(arr2)

# 3. Merge Sort - O(N*logN)

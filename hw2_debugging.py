import rand


def mergeSort(arr):
    if (len(arr) <= 1):
        return arr

    half = len(arr) // 2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = []
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    for i in range(rightIndex, len(rightArr)):
        mergeArr.append(rightArr[i])

    for i in range(leftIndex, len(leftArr)):
        mergeArr.append(leftArr[i])

    return mergeArr


arr = rand.random_array([None] * 20)
print("ip array:", arr)
arr_out = mergeSort(arr)
print("op array:", arr_out)
print(arr_out)

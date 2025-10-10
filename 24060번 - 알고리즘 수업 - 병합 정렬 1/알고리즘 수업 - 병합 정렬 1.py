#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24060                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24060                          #+#        #+#      #+#     #
#    Solved: 2025/10/10 01:34:56 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(200000)

input = sys.stdin.readline
output = sys.stdout.write

def find_value(value): # 저장에 따른 횟수와 value를 관히
    global k, save_counter, target_value

    # 호출 시
    save_counter += 1

    # 찾으려는 저장횟수가 되었을 때 값을 저장
    if save_counter == k:
        target_value = value

def merge_sort(arr, p, r): # 오름차순 정렬
    # 찾으려는 값을 이미 찾은 경우
    if target_value != -1:
        return
    
    if p >= r:
        return
    
    pivot = (p + r) // 2 # 피벗(기준점)
    merge_sort(arr, p, pivot) # 피벗을 기준으로 왼쪽 정렬
    merge_sort(arr, pivot + 1, r) # 오른쪽 정렬
    merge(arr, p, pivot, r) # 병합

def merge(arr, p, q, r):
    i, j = p, q+1
    tmp = [] # 임시 배열

    while i <= q and j <= r: # 병합할 서브리스트의 왼쪽, 오른쪽이 모두 남았을 떄
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    
    while i <= q: # 왼쪽 배열이 남은 경우
        tmp.append(arr[i])
        i += 1
    
    while j <= r: # 오른쪽 배열이 남은 경우
        tmp.append(arr[j])
        j += 1

    # 결과를 저장
    for index in range(len(tmp)):
        arr[p+index] = tmp[index]
        # 저장 되는 value
        find_value(tmp[index])

n, k = map(int, input().split())
save_counter = 0
target_value = -1
array = list(map(int, input().split()))
# 병합정렬
merge_sort(array, 0, len(array)-1)
output(str(target_value))
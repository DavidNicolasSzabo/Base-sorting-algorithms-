import random
import time
import csv
import sys
timelim1 = 30
timelim2 = 180
sys.setrecursionlimit(10**6)
def quicksort(arr, first, last, piv, time_limit, start_time, rec_limit):

    if sys.getrecursionlimit() - sys.getrecursionlimit() * 0.1 <= rec_limit:
        return "DNF-rec limit"
    if first < last:
        if time.time() - start_time >= time_limit:
            return "DNF"
        if piv == 1:
            pivot = pivot1(arr, first, last, time_limit, start_time)
            quicksort(arr, first, pivot - 1, piv, time_limit, start_time, rec_limit + 1)
            quicksort(arr, pivot + 1, last, piv, time_limit, start_time, rec_limit + 1)

def pivot1(arr, first, last, time_limit, start_time):
    # Middle pivot
    v = arr[(first + last) // 2]
    i = first - 1
    j = last

    while i < j:
        i += 1
        while arr[i] < v:
            i += 1
        j -= 1
        while arr[j] > v:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[last] = arr[last], arr[i]
    return (first+last)//2


def merge_sort(arr, first, last):
    if first < last:
        if time.time() - start_time >= time_limit:
            return "DNF"
        mid = (first + last) // 2
        merge_sort(arr, first, mid)
        merge_sort(arr, mid + 1, last)
        merge(arr, first, mid, last)

def merge(arr, first, mid, last):
    left_half = arr[first:mid + 1]
    right_half = arr[mid + 1:last + 1]

    i = j = 0
    k = first

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def insert_sort(arr,start_time):
    time_limit = 30
    if len(arr) > 10000:
        time_limit = 180


    for i in range(1, len(arr)):
        if time.time() - start_time >= time_limit:
            return "DNF"
        aux = arr[i]
        j = i - 1
        while j >= 0 and aux < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = aux
    return str(time.time() - start_time)

def selection_sort(arr,start_time):
    time_limit = 30
    if len(arr) > 10000:
        time_limit = 180
    for i in range(len(arr) - 1):
        if time.time() - start_time >= time_limit:
            return "DNF"
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return str(time.time() - start_time)

def bubble_sort(arr,start_time):
    time_limit = 30
    if len(arr) > 10000:
        time_limit = 180
    i = len(arr)
    while i >= 1:
        j = 0
        if time.time() - start_time >= time_limit:
            return "DNF"
        while j < i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i -= 1
    return str(time.time() - start_time)
def check(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

if __name__ == "__main__":
    with open("Data.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        lists_dict = {}
        lists_dict['list1'] = [random.randint(1, 100) for _ in range(10)]
        lists_dict['list2'] = [random.randint(1, 200) for _ in range(500)]
        lists_dict['list3'] = [random.randint(1, 3000) for _ in range(10000)]
        lists_dict['list4'] = [random.randint(1, 2000000) for _ in range(1000000)]
        lists_dict['list5'] = [random.randint(1, 4500000) for _ in range(10000000)]
        lists_dict['list6'] = [i for i in range(10)]
        lists_dict['list7'] = [i for i in range(500)]
        lists_dict['list8'] = [i for i in range(10000)]
        lists_dict['list9'] = [i for i in range(1000000)]
        lists_dict['list10'] = [i for i in range(10000000)]
        lists_dict['list11'] = [i for i in range(10)]
        lists_dict['list12'] = [i for i in range(500)]
        lists_dict['list13'] = [i for i in range(10000)]
        lists_dict['list14'] = [i for i in range(1000000)]
        lists_dict['list15'] = [i for i in range(10000000)]
        lists_dict['list11'].extend(lists_dict['list1'])
        lists_dict['list12'].extend(lists_dict['list2'])
        lists_dict['list13'].extend(lists_dict['list3'])
        lists_dict['list14'].extend(lists_dict['list4'])
        lists_dict['list15'].extend(lists_dict['list5'])
        lists_dict['list16'] = [[random.randint(1, 350) for _ in range(20)] for _ in range(20)]
        lists_dict['list17'] = [[random.randint(1, 350) for _ in range(20)] for _ in range(500)]
        lists_dict['list18'] = [[random.randint(1, 350) for _ in range(20)] for _ in range(10000)]
        lists_dict['list19'] = [[random.randint(1, 350) for _ in range(20)] for _ in range(200000)]
        lists_dict['list20'] = [[random.randint(1, 350) for _ in range(20)] for _ in range(20)]

        for i in lists_dict:
            l = []

            if len(lists_dict[i]) > 10000:
                time_limit = timelim2
            else:
                time_limit = timelim1
            start_time = time.time()
            test = lists_dict[i].copy()
            if i in ['list1', 'list2', 'list3', 'list4', 'list5', 'list6', 'list7', 'list8', 'list9', 'list10',
                     'list11', 'list12', 'list13', 'list14', 'list15']:
                if quicksort(test, 0, len(test) - 1, 1, time_limit, start_time,0) in ["DNF", "DNF-rec limit"]:
                    l.append("DNF")
                else:
                    if check(test):
                        l.append(str(time.time() - start_time))
                    else:
                        l.append(f"Not sorted correctly, time:{time.time() - start_time}",time.time() - start_time)
            else:
                if quicksort(test, 0, len(test) - 1, 1, time_limit, start_time,0) in ["DNF", "DNF-rec limit"]:
                    l.append("DNF")
                else:
                    if check(test):
                        l.append(str(time.time() - start_time))
                    else:
                        l.append(f"Not sorted correctly, time:{time.time() - start_time}",time.time() - start_time)

            start_time = time.time()
            test = lists_dict[i].copy()
            if merge_sort(test, 0, len(test) - 1) == "DNF":
                l.append("DNF")
            else:
                if check(test):
                    l.append(str(time.time() - start_time))
                else:
                    l.append(f"Not sorted correctly, time:{time.time() - start_time}",time.time() - start_time)

            start_time = time.time()
            test = lists_dict[i].copy()
            test_time5 = bubble_sort(test,start_time)
            if test_time5 == "DNF":
                l.append(test_time5)
            else:
                if check(test) == True:
                    l.append(test_time5)
                else:
                    l.append(f"Not sorted correctly, time:{test_time5}",test_time5)

            start_time = time.time()
            test = lists_dict[i].copy()
            test_time6 = insert_sort(test,start_time)
            if test_time6 == "DNF":
                l.append(test_time6)
            else:
                if check(test) == True:
                    l.append(test_time6)
                else:
                    l.append(f"Not sorted correctly, time:{test_time6}",test_time6)

            start_time = time.time()
            test = lists_dict[i].copy()
            test_time7 = selection_sort(test,start_time)
            if test_time7 == "DNF":
                l.append(test_time7)
            else:
                if check(test) == True:
                    l.append(test_time7)
                else:
                    l.append(f"Not sorted correctly, time:{test_time7}",test_time7)

            csvwriter.writerow(l)


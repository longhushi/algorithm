# 用Python写一个冒泡排序算法

def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return



# 用python写一个插入排序算法

def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        for i in range(j, 0, -1):
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else:
                break

import time

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)
    print(alist)
    baconFile = open('D:\\zj\\自己项目\\机器学习实战\\bacon.txt','a')
    baconFile.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'--->'+str(alist))
    baconFile.write('\n')
    baconFile.close()



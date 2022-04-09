
# ----------------反转字符串------------------------
# def resort(a):
#     s = []
#     for i in range(len(a)-1, -1, -1):
#         s.append(a[i])
#     return ''.join(s)  # 列表转字符串
#
#
# if __name__ == '__main__':
#     print(resort(a='dadsd'))
#
#
# def resort(a):
#     return a[::-1]  # 字符串切片
#
#
# if __name__ == '__main__':
#     print(resort(a="asdf"))
#
#
# def resort(a):
#     s = list(a)
#     s.reverse()  # 先转列表再reverse
#     return "".join(s)  # 再转回字符串
#
#
# if __name__ == '__main__':
#     print(resort(a="asd% ￥f"))


#  ---------------------------字符串转整数-------------------------------
# ord()以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值  如：#ord('a') 97

# def cal(a):
#     sum = 0
#     flag = 1
#     for i in range(len(a)):
#         if i == 0 and a[i] == "-":
#             flag = -1
#         elif "0" <= a[i] <= "9":
#             y = ord(a[i]) - ord("0")
#             sum = sum * 10 + y
#     return flag * sum
#
#
# if __name__ == '__main__':
#     print(cal(a="-a123"))


#  ---------------------------处理输入输出-------------------------------
# 1 2 3 4
# i = input().split()
# l = map(int, input().split())  # 先分割，再转换为int
# ll = map(int, input().strip().split())  # 先移除字符串首尾的字符，再分割
# def cal(a, target):
#     s = []
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[i] + a[j] == target:
#                 s.append([i, j])
#     return s
#
#
# if __name__ == '__main__':
#     print(cal(a=[1, 2, 3, 5, 6, 8, 9], target=8))

# --------------------------两数和为目标值------------------------------
# def cal(num, target):
#     s = []
#     for i, n in enumerate(num):
#         if target-n in num[i+1:]:
#             s.append([i, num[i+1:].index(target-n)+i+1])
#     return s
#
#
# if __name__ == '__main__':
#     print(cal(num=[1, 2, 3, 5, 4, 6, 8, 9], target=8))


# -----------------------快排---------------------------------

# def quicksort(num, start, end):
#     if start >= end:
#         return
#     left = start
#     right = end
#     mid = num[left]
#     while left < right:
#         while left < right and num[right] >= mid:
#             right -= 1
#         num[left] = num[right]
#         while left < right and num[left] < mid:
#             left += 1
#         num[right] = num[left]
#     num[left] = mid   # while结束后，把mid放在中间位置
#     quicksort(num, start, left-1)
#     quicksort(num, left+1, end)
#
#
# if __name__ == '__main__':
#     num = [2, 5, 6, 9, 3, 1]
#     quicksort(num=num, start=0, end=len(num)-1)
#     print(num)


# -------------------------反转32位有符号整数---------------------------
# def resort(num):
#     if num > 0:
#         resort_x = int(str(num)[::-1])
#     else:
#         resort_x = -int(str(num)[:0:-1]) # 第一个字符不参与倒序
#
#     if -2 ** 31 <= resort_x <= 2 ** 31 - 1:
#         return resort_x
#     else:
#         return 0
#
#
# if __name__ == '__main__':
#     # print(resort(num=23728478264738821928917179311))
#     print(resort(num=237284))

# -------------------------二分查找--------------------------
def search(num, a):
    mid = len(num) // 2
    left = 0
    right = len(num) - 1
    while left <= right:
        if a == num[mid]:
            return mid
        if a > num[mid]:
            left = mid + 1
        if a < num[mid]:
            right = mid - 1
        mid = (right + left) // 2  # 这里是加号！！
    return


if __name__ == '__main__':
    print(search(num=[1, 2, 3, 4, 5], a=4))


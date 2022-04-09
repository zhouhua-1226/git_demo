

# 最长连续子数组和  动态规划
# def maxSum(num):
#     dp = [0] * len(num)
#     dp[0] = num[0]
#     result = num[0]
#     for i in range(1, len(num)-1):
#         dp[i] = max(dp[i-1] + num[i], num[i])
#         result = max(result, dp[i])
#     return result
#
#
# if __name__ == '__main__':
#     print(maxSum(num=[-2,1,-3,4,-1,2,1,-5,4]))


# 单词反转，单词里的字母不反转
# def reverse(s):
#     s = s.split(" ")
#     result = []
#     for i in range(len(s)-1, -1, -1):
#         result.append(s[i])
#     return "".join(result)
#
#
# if __name__ == '__main__':
#     print(reverse(s="i am a student ."))
#
# x = 20
# print(hex(x))  # 转16进制
# print(oct(x))  # 转8进制


# a = "asdfgh"
# b = "asrfgt"
# s = []
# for i in range(len(a)):
#     if ord(a[i]) == ord(b[i]):
#         s.append(0)
#     elif ord(a[i]) > ord(b[i]):
#         s.append(-1)
#     else:
#         s.append(1)
# print(s)

# 三元表达式 y=1 if s>3 else 9

# # 冒泡排序
# a = [2, 3, 1, 6, 5, 4]
# if len(a) < 2:
#     print(a)
# for i in range(len(a)-1):
#     for j in range(len(a)-1-i):
#         if a[j] > a[j+1]:
#             a[j+1], a[j] = a[j], a[j+1]
# print(a)

# 判断链表中是否有环
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# def cycle(head):
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#     return False
#
#
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = head.next
# print(cycle(head))  # True


#  找出字符串中第一个不重复的字符及位置
# def search(a):
#     dict = {}
#     for i in range(len(a)):
#         if a[i] in dict:
#             dict[a[i]] += 1
#         else:
#             dict[a[i]] = 1
#     for i in range(len(a)):
#         if dict[a[i]] == 1:
#             return a[i], i+1
#
#
# if __name__ == '__main__':
#     print(search(a="abssdab"))

# 二叉树的前序遍历，用迭代：栈
# def preorder(root):
#     stack = [root]
#     res = []
#     if not root:
#         return []
#     while stack:
#         top = stack.pop()
#         res.append(top.data)
#         if top.right:
#             stack.append(top.right)
#         if top.left:
#             stack.append(top.left)
#     return res

# class BinaryTree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def get(self):
#         return self.data
#
#     def getLeft(self):
#         return self.left
#
#     def getRight(self):
#         return self.right
#
#     def setLeft(self, node):
#         self.left = node
#
#     def setRight(self, node):
#         self.right = node

# binaryTree = BinaryTree(0)
# binaryTree.setLeft(BinaryTree(1))
# binaryTree.setRight(BinaryTree(2))
# binaryTree.getLeft().setLeft(BinaryTree(3))
# binaryTree.getLeft().setRight(BinaryTree(4))
# binaryTree.getRight().setLeft(BinaryTree(5))
# binaryTree.getRight().setRight(BinaryTree(6))


# 二叉树的中序遍历
# result = []
# def midorder(root):
#     if not root:
#         return result
#     midorder(root.left)
#     result.append(root.data)
#     midorder(root.right)
#     return result


# if __name__ == '__main__':
#     print(midorder(binaryTree))


# 合并有序链表,递归
# def merge(l1, l2):
#     if not l1: return l2
#     if not l2: return l1
#     if l1.val <= l2.val:
#        l1.next = merge(l1.next, l2)
#        return l1
#     else:
#        l2.next = merge(l1, l2.next)
#        return l2
#
#
# if __name__ == '__main__':
#     class ListNode:
#         def __init__(self, x):
#             self.val = x
#             self.next = None
#     l1 = ListNode(1)
#     l1.next = ListNode(2)
#     l1.next.next = ListNode(4)
#     l2 = ListNode(1)
#     l2.next = ListNode(3)
#     l2.next.next = ListNode(4)
#     p = merge(l1, l2)
#     while p:
#         print(p.val)
#         p = p.next


# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,
# def func(num):
#     if num <= 1:
#         return num
#     else:
#         return func(num-2)+func(num-1)
#
#
# for i in range(8):  # 输出前8个
#     print(func(i))


# 反转单向链表
# def reverse_single(head):
#     pre = None
#     while head:
#         tmp = head.next
#         head.next = pre
#         pre = head
#         head = tmp
#     return pre
#
#
# # 反转双向链表
# def reverse_double(head):
#     pre = None
#     while head:
#         next = head.next
#         head.next = pre
#         head.pre = next
#         pre = head
#         head = next
#     return pre


# [1,2,3,3,3,4,5] target=3
# 输出[2,4]
# def search(a, target):
#     s = []
#     for i in range(len(a)):
#         if a[i] == target:
#             s.append(i)
#             print(s)
#     if not len(s):
#         return [-1, -1]
#     else:
#         return [s[0], s[-1]]
#
#
# if __name__ == '__main__':
#     print(search(a=[1], target=1))


# def search(a, target):
#     start = 0
#     end = len(a)-1
#     while start <= end:  # 二分查找
#         mid = (start + end) // 2
#         if target < a[mid]:
#             end = mid - 1
#         elif target > a[mid]:
#             start = mid + 1
#         else:
#             break
#     else:
#         return [-1, -1]
#     for i in range(mid, len(a)):  # 确定右边界
#         if a[i] != target:
#             end = i - 1
#             break
#     for i in range(mid, -1, -1):  # 确定左边界
#         if a[i] != target:
#             start = i+1
#             break
#     return [start, end]
#
#
# if __name__ == '__main__':
#     print(search(a=[1,2,3,3,3,4,5], target=3))


# 排序数组去重：双指针
# [1,1,2,3,4,4] 输出4
# def del_double(a):
#     i = 0
#     j = 1
#     while j < len(a):
#         if a[i] == a[j]:
#             j += 1
#         else:
#             i += 1
#             a[i] = a[j]
#             j += 1
#     return i+1
#
#
# if __name__ == '__main__':
#     print(del_double(a=[1,1,1,2,3,4,4,5]))

# k个一组反转链表
# def reverse(self, head, tail):
#     prev = tail.next
#     p = head
#     while prev != tail:
#         next = p.next
#         p.next = prev
#         prev = p
#         p = next
#     return tail, head
#
# def reverseKGroup(self, head, k):
#     hair = ListNode(0)
#     hair.next = head
#     pre = hair
#     while head:
#         tail = pre
#         # 查看剩余部分长度是否大于等于k
#         for i in range(k):
#             tail = tail.next
#             if not tail:
#                 return hair.next
#         next = tail.next
#         head, tail = self.reverse(head, tail)
#         # 把子链表重新接回原表
#         pre.next = head
#         tail.next = next
#         pre = tail
#         head = tail.next
#     return hair.next

# [1, 2, 4, 4, 5]  4  查找第一个大于4的值
# def search(a, target):
#     start = 0
#     end = len(a) - 1
#     while start < end:
#         mid = (start + end) // 2
#         if a[mid] < target:
#             start = mid + 1
#         else:
#             end = mid
#     return start
#
#
# if __name__ == '__main__':
#     print(search(a=[2, 4, 4, 5], target=4))
y = "j:2"
x = "j:-2 x:3"
s = y.split(":")
c =[]
sum = 0
for i in range(int(s[1])):
    a = x.split()[i].split(":")
    c.append(int(a[1]))
for i in range(2):
    sum = sum+ c[i]
print(sum)
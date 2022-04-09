# 两个栈实现队列
class stack_que():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push_que(self, x):
        self.stack1.append(x)

    def pop_que(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            if self.stack1:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
            else:
                return None


if __name__ == '__main__':
    s = stack_que()
    s.push_que(x=[1, 2, 3, 4])
    print(s.pop_que())




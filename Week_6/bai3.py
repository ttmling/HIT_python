class Stack:
    def __init__(self):
        self.stack = []
        self.capacity = 0
    
    def initialization(self, capacity):
        self.stack = []
        self.capacity = capacity
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.capacity
    
    #loại bỏ top element và trả về giá trị đó
    def pop(self):
        if self.isEmpty():
            print("Stack rỗng.")
            return
        value = self.stack.pop()
        return value
    
    #add thêm value vào trong stack
    def push(self, val):
        if self.isFull():
            print("Stack đầy.")
            return
        self.stack.append(val)

    #lấy giá trị top element mà không loại bỏ nó
    def top(self):
        if self.isEmpty():
            print("Stack rỗng.")
            return
        return self.stack[-1]
    
    def printStack(self):
        if self.isEmpty():
            print("Stack rỗng.")
            return
        print("Stack:")
        for i in reversed(self.stack):
            print(i)


s = Stack()
s.initialization(5)
s.push(1)
s.push(2)
s.printStack()

print(f"Kiểm tra đầy: {s.isFull()}")

print(f"Lấy giá trị cuối: {s.top()}")
s.printStack()


print(f"Lấy giá trị cuối và xóa: {s.pop()}")
s.printStack()
num = 42

def f():
    global num
    num = 100


f()
print(num)
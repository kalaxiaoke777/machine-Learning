# def my_decorator(cd):
#     def my_decorator(func):
#         def wrapper():
#             print(f"我想在之前做些什么。。。。。{cd}")
#             func()
#             print("我想在之后做些什么。。。。。")
#         return wrapper
#     return my_decorator
#
# @my_decorator(32)
# def say_hello():
#     print("Hello!")
#
# say_hello()
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(x, y, data):
    return x + y

result = add(3, 5, data={"aef":1})
# 输出: Function 'add' called with arguments: (3, 5) {}
print(result)  # 输出: 8
# def uppercase_decorator(func_txt)
#     def upper_txt(letter)
#         text = str(func_txt())
#         return text.upper()
#     return upper_txt


def uppercase_decorator(txt_func):
    def nested():
        txt = txt_func()
        txt = txt.upper()
        return txt
    return nested

@uppercase_decorator
def say_hello():
    return "hello"

@uppercase_decorator
def say_hi():
    return "hihihiih"

print(say_hello())
print(say_hi())
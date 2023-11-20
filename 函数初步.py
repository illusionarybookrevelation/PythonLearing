def function(a,b=8):
    print(a)
    print(b)
function(1)     #形参未传递实参时以默认值为主，有实参传递时以实参为准
function(1,2)

#定义函数内部变量为全局变量
def func3():
    global i
    i=7
func3()
print(i)
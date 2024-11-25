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

#LEGB法则
range=8
def func1():
    ranne=9
    def func2():
        range=6
        print(range)
    func2()
func1()

#单个返回值
def test():
    i=7
    i+=1
    return i
print(test())

#多个返回值
def funcrtn(i,j):
    k=i*j
    return (i,j,k)
x=funcrtn(4,5)#返回值第一种接受方式
print(x)
a,b,c=funcrtn(7,8)#返回值第二种接受方式
print(a)
print(b)
print(c)

#文档字符串
def d(i,j):
    '''这个函数实现了一个乘法运算


    函数会返回一个乘法运算的结果'''
    k=i*j
    return k
print(d.__doc__)   #第一种调用方法
print(help(d)) #第二种调用方法
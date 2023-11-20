#算术运算符
#(1)加法
a=7+8
print(a)
b="GOOD"+"JOB!"
print(b)

#(2)减法
c=-7
print(c)
d=19-1
print(d)

#(3)乘法
e=4*7
print(e)
f="hello"*5
print(b)

#(4)除法
g=7/2
print(g)

#(5)幂
h=2**3
print(h)

#(6)整除
i=10//3
print(i)

#(7)求余
j=10%3
print(j)

#比较运算符
#(1)等于
k=12==13
print(k)
l="hello"=="hello"
print(l)

#(2)不等于
m=2!=3
print(m)
n=2!=2
print(n)

#(3)小于等于
o=3<=3
print(o)
p=4<=3
print(p)

#(4)大于等于
q=1>=3
print(q)
r=4>=3
print(r)

#逻辑运算
#(1)逻辑非
t=True
u=not t
print(u)
v=False
print(not v)

#(2)逻辑与
#True and True 等于 True
#True and False 等于 False
#False and False 等于 False
print(True and True)

#(3)逻辑或
#True and True 等于 True
#True and False 等于 True
#False and False 等于 False
print(True and False)

#按位运算，将数据转化位二进制然后进行与运算，结果再转化为十进制
#(1)按位与
w=7&18
print(w)

#(2)按位或
x=7|18
print(x)

#(3)按位异或
y=7^18
print(y)

#(4)按位翻转
z=~18 #~18=-(18+1)=-19
print(z)

#左移与右移运算，将原来的数字转换为二进制后进行移位
A=18<<1 #左移一个单位相当乘以2，两个单位乘以4，n个单位乘以2的n次幂
print(A)
B=18>>1 #右移一个单位相当除以2，两个单位除以4，n个单位除以2的n次幂
print(B)

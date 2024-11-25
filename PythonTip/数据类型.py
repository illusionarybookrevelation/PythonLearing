a=19
b=19.0
print(type(a))
print(type(b))

#列表
student=["小明","小华","小李","小娟","小云"]
print(student[3])
#列表元素替换
student[2]='小月'
print(student)

#元组，与列表不同的是元组里面的元素不能修改
student=("小明","小军","小强","小武","小艺")
print(student)
print("第一位成员是："+student[0])

#集合，集合内不允许存在重复的元素，然后它具有去重功能
#第一种创建集合的方式
cop=set("abcd")
print(cop)
#第二种创建集合的方式
cap={5,"python","php"}
print(cap)

get=set("abcnmaaaaggsng")
post=set("cdfm")
#交集，可以通过&符号实现交集运算
x=get&post

#并集，可以通过|符号实现并集运算
y=get|post

#差集，可以通过-符号实现差集运算
z=get-post
print("集合get是："+str(get))#因为集合不能直接进行字符串连接，所以需要强行转换为字符串
print("集合post是："+str(get))
print("get与post的交集是："+str(x))
print("get与post的并集是："+str(y))
print("get与post的差集是："+str(z))

#字典，也叫关联数组
k={"姓名":"韦玮","籍贯":"桂林"}
print(k)
#往字典里添加新的元素
print("籍贯是："+k["籍贯"])
k["爱好"]="音乐"
print("姓名为："+k["姓名"])
print("爱好为："+k["爱好"])
#Python内置对象主要有数字、字符串、列表、元组、字典、集合等
#如果有一些对象需要持久性存储，并且保证这个对象的类型与数据不会丢失，则需要将这些对象进行序列化
#序列化的这种过程称为pickle（腌制）
"""
pickle中的方法主要有：
(1)dumps(object)
(2)loads(string)
(3)dump(object,file)
(4)loads(file)
"""
#pickle腌制
import pickle
lista=["Python","PHP","机器学习"]
#dumps(object)将对象序列化
listb=pickle.dumps(lista)
print(listb)
#loads(string)将对象原样恢复，对象类型格式也恢复为原来的格式
listc=pickle.loads(listb)
print(listc)

#dump(object,file)序列化存储到文件中
t1=["Python","PHP","机器学习"]
f1=open('D:/Python/t1.pk1','wb')
pickle.dump(t1,f1,True)
f1.close()

#load(object,file)将文件里的数据恢复
f2=open('D:/Python/t1.pk1','rb')
t=pickle.load(f2)
print(t)
f2.close()
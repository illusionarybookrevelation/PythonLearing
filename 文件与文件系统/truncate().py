fu = open(r'./tt.txt','r+')
print("文件名为：",fu.name)
line = fu.readline()
print("读取数据为：%s" % line)
fu.truncate()
line = fu.readlines()
print("当前位置为：%s" % line)
fu.close()


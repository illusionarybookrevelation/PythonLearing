# 简单来说他们的效果是把读到的数据统一存在一个列表中，而readfile和writefile是对整个数据进行读写操作
# readfills和writefiles组合修改数据
file = open(r'./tm.txt',"r+")
print("文件名为：",file.name)
str_lines = file.readlines()
file.close()

str_lines[1] = "乱山高下路东西 \n"
file = open(r'./tm.txt',"w+")
file.writelines(str_lines)
file.close()


# fileObject.seek(offset[,whence])
# 参数offset表示开始的偏移量，即需要移动偏移的字节数；参数whence为可选参数，表示从哪个位置开始偏移，默认值为0
fu = open(r'./tt.txt','r+')
print("文件名为：",fu.name)
line = fu.readline()
print("读取数据为：%s" % line)

fu.seek(0,0)

line = fu.readline()
print("读取的数据为：%s" % line)
fu.close()
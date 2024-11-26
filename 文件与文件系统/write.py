fu = open(r'./te.txt',"r+")
print("文件名为：",fu.name)
str = "将飞更作回风舞，已落犹成半面妆。"

fu.seek(0,2)
line = fu.write(str)
fu.seek(0,0)
print(fu.read())
fu.close()
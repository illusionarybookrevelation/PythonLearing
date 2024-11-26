file = open(r'./to.txt',"r+")
file_save = file.read()
file.close()

file_a = open(r'./tk.txt',"a")
file_a.write(file_save)
file_a.flush()
file.close()

file_read = open(r'./tk.txt',"r")
print(file_read.read())
file_read.close()
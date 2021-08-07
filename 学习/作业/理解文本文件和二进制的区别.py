#理解文本文件和二进制的区别
textFile = open("7.1.txt", "rt")  # 用二进制的方式打开7.1
print(textFile.readline())
textFile.close()
binFile = open("7.1.txt", "rb")
print(binFile.readline())
binFile.close()
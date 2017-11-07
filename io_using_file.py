poem = """\
这里是备注。。。。。。
。。。。。。。。
。。。。。。



"""

# 打开文件以编辑（'w'riting）
f = open('poem.txt','w')
# 向文件中编辑文本
f.write(poem)
#关闭文件
f.close()


# 如果没有特别指定
# 将假定启用默认的阅读（'r'ead）模式
f = open('poem.txt')
while True:
	line = f.readline()
	# 零长度指示 EOF
	if len(line) == 0:
		break
	# 每行('line')的末尾
	# 都已经有了换行副
	# 因为它是从一个文件中运行读取的
	print(line,end='')
# 关闭文件
f.close()
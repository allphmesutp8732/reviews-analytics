data = []
count = 0
read = 0
len_data = 0
with open("reviews.txt", "r") as a:
	for line in a:
		data.append(line)

print("檔案讀取完畢，本檔案共有",len(data),"筆留言")


wc = {} #word_count
for d in data:
	words = d.split(" ")
	for word in words:
		if word in wc:
			wc[word] += 1
		elif word == "." or word == ",":
			continue
		else:
			wc[word] = 1
print("字典建構完成！")
while True:
	word = input("請輸入想查的字")
	if word == "q":
		print("感謝使用")
		break
	elif word in wc:
		print(word, "共出現", wc[word], "次")
	else:
		print("這個字沒有出現過喔！")




# for cm in data:
# 	len_data = len_data + len(cm)
# print("平均字數為",len_data/len(data))

# #while read > -5:
# #	print("This is comment no.",1000000+read)
# #	print(data[read])
# #	read -= 1

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('共有',len(new),'筆留言數 < 100')

# search_good = []
# for d in data:
# 	if 'good' in d:
# 		search_good.append(d)
# print('共有',len(search_good),'筆留言中含有"Good"')
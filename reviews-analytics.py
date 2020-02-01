data = []
count = 0
read = 0
len_data = 0
with open("reviews.txt", "r") as a:
	for line in a:
		data.append(line)

print("檔案讀取完畢，本檔案共有",len(data),"筆留言")

for cm in data:
	len_data = len_data + len(cm)
print("平均字數為",len_data/len(data))

#while read > -5:
#	print("This is comment no.",1000000+read)
#	print(data[read])
#	read -= 1

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有',len(new),'筆留言數 < 100')
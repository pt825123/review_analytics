data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')


for d in data:
	sum_len += len(d)
average = sum_len / len(data)
print('平均留言長度為', average)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')


# 文字計數

wc = {}
for d in data:
	words = d.split() # split()預設引數為空白鍵，且不會留下空字串
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你想查什麼字?')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('這個字沒有出現過!')

print('感謝使用本查詢功能')












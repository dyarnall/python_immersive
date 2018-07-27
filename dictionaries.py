d = {}
word = "applleeee"
cnt = 0

for i in word:
	d[i] = d.get(i,1) + 1

# 	if i in d:
# 		d[i] += 1
# 	else:
# 		d[i] = 1	
print(d)

	
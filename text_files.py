dic = {}
fakelist = ["wonder.", "help!", ".nope"]

def split_char(word):
	my_string = ["?", ".", ",", "!"]

	for f in word:
		if f in my_string:
			#print("f", f)
			#print("word", word)
			word = word.strip(f)
			#print("final",word)
	return word

def unpacking(tup):
	return tup[1]

def counter(data):
	for word in data:
		word = split_char(word)
		dic[word] = dic.get(word,0) + 1

def main():
	with open('article.txt','r', encoding="utf-8") as article:
		data = article.read().lower().split()
		#print(data[:30])
		counting = counter(data)

		alist = list(dic.items())
		alist.sort(key=unpacking, reverse=True)
		print(alist[:20])

main()



		
		





# word1 = input("enter word 1: ")
# word2 = input("enter word 2: ")
# d1 = {}
# d2 = {}

# for i in word1:
# 	d1[i] = d1.get(i,1) + 1
# for i in word2:
# 	d2[i] = d2.get(i,1) + 1
# if d1 == d2:
# 	print(word1, "and", word2, "are anagrams.")
# else:
# 	print(word1, "and", word2, "are not anagrams.")


def counter(word):
	d = {}
	for i in word:
		d[i] = d.get(i,1) + 1
	return d
	
def anagrams():
	word1 = user_input()
	word2 = user_input()

	d1 = counter(word1)
	d2 = counter(word2)

	if d1 == d2:
	print(word1, "and", word2, "are anagrams.")
	else:
	print(word1, "and", word2, "are not anagrams.")

def user_input():
	word = input("enter a word: ")
	return word
alist = [1,2,3,4,5]
elist = list(enumerate(alist))

print(alist)
print(elist)

print("change the count:")
dlist = list(enumerate(alist,10))
print(dlist)


print("the range way:")
for i in range(len(alist)):
	print(alist[i],end="")

print()

print("enumerate way")
for count,i in enumerate(alist):
	print(i,end="")





s="abc"
list=[]
for i in s:
	list.append(i)
	for k in s:
		if i!=k:
			list.append((i,k))
		for j in s:
			if (i!=k) & (i!=j) &(k!=j) &(i!=j!=k):
				list.append((i,k,j))


list1=[]
for i in s:
	list1.append(i)

list2=[]
for i in list1:
	for k in s:
		if i!=k:
			list2.append(i+k)	
list3=[]
for i in list2:
	for k in s:
		if k not in i:
			list3.append(i+k)
print(list1+list2+list3)




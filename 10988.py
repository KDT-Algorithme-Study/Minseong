palindrom = input()
palindrom_list = []
palindrom_list2 = []

for i in range(len(palindrom)):
    palindrom_list.append(palindrom[i])

for j in range(len(palindrom)):
    palindrom_list2.append(palindrom[i-j])
    
if palindrom_list == palindrom_list2:
    print(1)
else:
    print(0)  
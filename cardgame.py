card_set1 = input()
card_set2 = input()


list1 = []
for i in card_set1:
    list1.append(i)

list2 = []
for i in card_set2:
    list2.append(i)



if (list1[0] == "d"  or list2[0] == "d") and (list1[2] == "d"  or list2[2] == "d") and (list1[1] == "a"  or list2[1] == "a"):
    print("yes")
    
else:
    print ("no")
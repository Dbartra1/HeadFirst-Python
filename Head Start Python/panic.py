phrase = "don't panic!"
#change phrase into a list 
plist = list(phrase)
#print phrase and list
print (phrase)
print (plist)
#for loop to take out the last 4 items in the list
for i in range(4):
    plist.pop()
#remove the new letter in position 0
plist.pop(0)
#remove the '
plist.remove("'")
#poping out the last two objects and using them to extend the list
plist.extend([plist.pop(), plist.pop()])
#remove the space in position 3 and reinsert it in position 2
plist.insert(2, plist.pop(3))

#making the list back into a string phrase
new_phrase = ''.join(plist)
print (plist)
print (new_phrase)